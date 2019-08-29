class Graph:
    def __init__(self, e=[]):
        self.edges = e

    def __repr__(self):
        a = []
        for u, v, w in self.edges:
            a.append("%i --> %i = %.2f" % (u, v, w))
        return " | ".join(a)

    def add_edge(self, u, v, w=0.0):
        """ Add an edge from node u to node v

        @u: [int] indexing source node
        @v: [int] indexing target node
        @w: [float] The weight for the edge. Defaults to 0.0
        """
        self.edges.append((u, v, w))


class AdjListGraph(Graph):
    def __init__(self, n=0, e={}):
        self.nodes = n
        self.edges = e

    def __repr__(self):
        return str(self.edges)

    def add_edge(self, u, v, w=0.0):
        """ Add an edge from node u to node v

        @u: [int] indexing source node
        @v: [int] indexing target node
        @w: [float] The weight for the edge. Defaults to 0.0
        """
        self.edges[u] = (v, w)


class AdjMatrixGraph(Graph):
    def __init__(self, n=0, e=[[]]):
        self.nodes = n
        self.edges = [[0.0] * self.nodes for i in range(self.nodes)]

    def __repr__(self):
        return '\n'.join([' '.join([str(c) for c in row]) for row in self.edges])

    def add_edge(self, u, v, w=0.0):
        """ Add an edge from node u to node v

        @u: [int] indexing source node
        @v: [int] indexing target node
        @w: [float] The weight for the edge. Defaults to 0.0
        """
        n = max(u+1, v+1, self.nodes)
        if self.nodes < n:
            diff = n - self.nodes
            # Add the correct number of new cols
            for e in self.edges:
                e += [0.0] * diff
            # Add the correct number of new rows
            for d in range(diff):
                self.edges.append([0.0] * n)
            # Update num of nodes
            self.nodes = n
        self.edges[u][v] = w
