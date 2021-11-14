from numpy.core.fromnumeric import transpose
from numpy.core.numeric import Inf
from numpy.lib.npyio import load
import numpy as np
import math
import heapq

WHITE = "white"
GRAY = "gray"
BLACK = "black"

class Node:
    def __init__(self,i,n,source=False):
        self.index = i
        self.name = n
        if(source):
            self.d = 0
        else:
            self.d = math.inf
        self.p = None
    def __str__(self):
        return f"{self.name} costs {self.d} from {self.p}"
    def __eq__(self, o):
        return self.d == o.d and self.index == o.index
    def __gt__(self,o):
        return self.d > o.d
    def __lt__(self,o):
        return self.d < o.d

class NodeDFS:
    def __init__(self,i,n):
        self.index = i
        self.name = n
        self.p = None
        self.color = WHITE
    def started(self,s):
        self.s = s
    def finished(self,f):
        self.f = f
    def __str__(self):
        return f"{self.name} from {self.p}"
    def __eq__(self, o):
        return self.index == o.index
    def __gt__(self,o):
        return self.f > o.f
    def __lt__(self,o):
        return self.f < o.f


def getIndex(keys, k):
    if(not (k in keys)):
        keys.append(k)
    return keys.index(k)

def getKey(keys,i):
    if(i<len(keys)):
        return keys[i]
    else:
        return None

def loadGraph(fileName="sample2.txt"):
    fileTxt = open(fileName, "r").read()
    lines = fileTxt.splitlines()
    l = lines[0].split(" ")
    n = int(l[0])
    graph = np.zeros((n,n))
    keys = []
    undirected = l[2] == "U" or l[2] == "u"
    lines.remove(lines[0])
    startingNode = None
    for l in lines:
        h = l.split(" ")
        if(len(h) == 3):
            i1 = getIndex(keys,h[0])
            i2 = getIndex(keys,h[1])
            graph[i1,i2] = h[2]
            if(undirected):
                graph[i2,i1] = h[2]
        else:
            startingNode = h[0]
    if(startingNode == None):
        startingNode = keys[0]
    return (graph, keys, startingNode)

def relax(graph,u,v):
    if(v.d > u.d + graph[u.index,v.index]):
        v.d = u.d + graph[u.index,v.index]
        v.p = u

def dijkstras(graph,keys,source):
    #initialize-single-source
    Q = []
    for k in keys:
        i = getIndex(keys,k)
        if(k == source):
            heapq.heappush(Q,Node(i,k,True))
        else:
            heapq.heappush(Q,Node(i,k))
    S = []
    while(len(Q) > 0):
        u = heapq.heappop(Q)
        S.append(u)
        for v in Q:
            if(graph[u.index,v.index] > 0):
                relax(graph,u,v)
                heapq.heapify(Q)
    return S

def prim(graph,keys,source):
    #initialize-single-source
    Q = []
    for k in keys:
        i = getIndex(keys,k)
        if(k == source):
            heapq.heappush(Q,Node(i,k,True))
        else:
            heapq.heappush(Q,Node(i,k))
    S = []
    while(len(Q) > 0):
        u = heapq.heappop(Q)
        S.append(u)
        for v in Q:
            if(graph[u.index,v.index] > 0):
                if(graph[u.index,v.index] < v.d):
                    v.d = graph[u.index,v.index]
                    v.p = u
                    heapq.heapify(Q)
    return S

def dfsVisit(graph,G,u,time,printSCC=False):
    time += 1
    u.started(time)
    u.color = GRAY
    if(printSCC):
        print(u.name,end='')
    for v in G:
        if(graph[u.index,v.index] > 0 and v.color == WHITE):
            v.p = u
            time = dfsVisit(graph,G,v,time,printSCC)
    u.color = BLACK
    time +=1
    u.finished(time)
    return time


def stronglyConnected(graph,keys):
    G = []
    for k in keys:
        i = getIndex(keys,k)
        G.append(NodeDFS(i,k))
    time = 0
    for u in G:
        if(u.color == WHITE):
            dfsVisit(graph,G,u,time)
    Gp = np.sort(G).tolist()
    Gp.reverse()
    graphP = transpose(graph)
    for u in Gp:
        u.color = WHITE
        u.s = -1
        u.f = -1
    time = 0
    for u in Gp:
        if(u.color == WHITE):
            dfsVisit(graphP,Gp,u,time,True)
            print("")

(graph,keys, startingNode) = loadGraph()
sssp = dijkstras(graph,keys,startingNode)
print("Single-Source Shortest Paths (showing total costs at each node)")
for s in sssp:
    print(s)
print("Minimum Spanning Tree (showing edge cost from previous node)")
mst = prim(graph,keys,startingNode)
for s in mst:
    print(s)
stronglyConnected(graph,keys)