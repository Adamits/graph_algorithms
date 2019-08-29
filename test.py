from graph import *

def testAddEdge(g):
    g.add_edge(0, 1, 0.2)
    g.add_edge(0, 2, 0.5)
    g.add_edge(2, 1, 0.4)
    print(g)

if __name__=='__main__':
    g = Graph()
    testAddEdge(g)
    g = AdjListGraph()
    testAddEdge(g)
    g = AdjMatrixGraph()
    testAddEdge(g)
