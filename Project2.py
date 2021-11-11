from numpy.lib.npyio import load
import numpy as np

def getKey(keys, k):
    if(not (k in keys)):
        keys.append(k)
    return keys.index(k)

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
            i1 = getKey(keys,h[0])
            i2 = getKey(keys,h[1])
            graph[i1,i2] = h[2]
            if(undirected):
                graph[i2,i1] = h[2]
        else:
            startingNode = h[0]
    return (graph, keys, startingNode)


(graph,keys, startingNode) = loadGraph()
print(keys)
print(graph)
