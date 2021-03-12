import math
class Node():
    def __init__(self):
        self.cost = math.inf
        self.parent = None
        self.index = -1
        self.adjacent = []
        self.counted = False

    def sum(self):
        self.counted = True
        s = self.cost
        for i in range(len(self.adjacent)):
            if self.adjacent[i].counted == False:
                s += self.adjacent[i].sum()
        return s
class Graph():

    def __init__(self, adjacency_matrix):
        """
        Graph initialized with a weighted adjacency matrix

        Attributes
        ----------
        adjacency_matrix : 2D array
            non-negative integers where adjacency_matrix[i][j] is the weight of the edge i to j,
            with 0 representing no edge

        """

        self.adjacency_matrix = adjacency_matrix

        # Add more class variables below as needed, such as n:
        self.N = len(adjacency_matrix)



    def Prim(self):
        """
        Use Prim-Jarnik's algorithm to find the length of the minimum spanning tree starting from node 0

        Returns
        -------
        int
            Weighted length of tree

        """
        Q = []
        for i in range(self.N):
            vertex = Node()
            vertex.index = i
            Q.append(vertex)
        for k in range(len(Q)):
            for h in range(self.N):
                if self.adjacency_matrix[k][h] > 0:
                    Q[k].adjacent.append(Q[h])
        Q[0].cost = 0
        A = Q[0]
        while len(Q) != 0:
            u = Q.pop(0)
            for j in range(len(u.adjacent)):
                v = u.adjacent[j]
                e = self.adjacency_matrix[u.index][v.index]
                if v in Q and e < v.cost:
                    v.parent = u
                    v.cost = e
        sum = A.sum()
        return sum

#  Example use case:

G = Graph([[0, 10, 11, 33, 60],
           [10, 0, 22, 14, 57],
           [11, 22, 0, 12, 17],
           [33, 14, 12, 0, 9],
           [60, 57, 17, 9, 0]])
assert G.Prim() == 42
G = Graph([[0, 1, 3, 2, 0, 0],
           [1, 0, 0, 0, 0, 0],
           [3, 0, 0, 4, 5, 0],
           [2, 0, 4, 0, 6, 7],
           [0, 0, 5, 6, 0, 0],
           [0, 0, 0, 7, 0, 0]])
assert G.Prim() == 18
