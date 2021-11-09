from numpy.lib.npyio import load
import pandas as pd

def loadGraph(fileName="sample.txt"):
    cols = ["from","to","cost"]
    graph = pd.DataFrame(columns=cols)
    fileTxt = open(fileName, "r").read()
    lines = fileTxt.splitlines()
    l = lines[0]
    h = l.split(" ")
    undirected = h[2] == "U" or h[2] == "u"
    lines.remove(lines[0])
    startingNode = None
    for l in lines:
        h = l.split(" ")
        if(len(h) == 3):
            graph = graph.append({"from":h[0],"to":h[1],"cost":h[2]},ignore_index=True)
            if(undirected):
                graph = graph.append({"from":h[1],"to":h[0],"cost":h[2]},ignore_index=True)
        else:
            startingNode = h[0]
    # print(graph)
    # print(f"Starting Node: {startingNode}")
    return (graph,startingNode)

(graph, startingNode) = loadGraph()
