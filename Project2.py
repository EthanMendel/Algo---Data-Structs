from numpy.core.numeric import Inf
from numpy.lib.npyio import load
import numpy as np
import math
import heapq

class Node:
    def __init__(self,i,source=False):
        self.index = i
        if(source):
            self.d = 0
        else:
            self.d = math.inf
        self.p = None
    def __str__(self):
        return f"{self.index} costs {self.d} from parent {self.p}"
    def __eq__(self, o):
        return self.d == o.d and self.index == o.index
    def __gt__(self,o):
        return self.d > o.d
    def __lt__(self,o):
        return self.d < o.d


def getIndex(keys, k):
    if(not (k in keys)):
        keys.append(k)
    return keys.index(k)
def getKey(keys,i):
    if(i<len(keys)):
        return keys[i]
    else:
        return None

def loadGraph(fileName="sample.txt"):
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
    return (graph, keys, startingNode)

def relax(graph):
    pass

def dijkstras(graph,keys,source):
    #initialize-single-source
    Q = []
    for k in keys:
        i = getIndex(keys,k)
        if(k == source):
            heapq.heappush(Q,Node(i,True))
        else:
            heapq.heappush(Q,Node(i))
    S = []
    while(len(Q) > 0):
        u = heapq.heappop(Q)
        S.append(u)
        for k in keys:
            v = getIndex(keys,k)
            if(graph[u.index,v] > 0):
                relax(graph,u.index,v)

(graph,keys, startingNode) = loadGraph()
dijkstras(graph,keys,startingNode)