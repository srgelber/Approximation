##Simon Gelber - CSC359 Asgn 4
# Identify Vertex Covers
import sys
import copy
import random
from itertools import permutations
from collections import defaultdict

class Graph:

    def __init__(self):
        #Dictionary to store graph
        self.graph = defaultdict(list)

        #Number of vertices
        self.numV = 0

        self.numE = 0

    def add_edge(self, v, u):
        self.graph[v].append(u)

    def remove_value(self, value):
        newgraph = Graph()

        for vertex2 in self.graph:
            if vertex2 != value:
                for edge in self.graph[vertex2]:
                    if edge != value:
                        newgraph.graph[vertex2].append(edge)
        self.graph = newgraph.graph

    def getmaxdegree(self):
        maxdegreeVertex = 0
        for vertex in self.graph.copy():
            if len(self.graph[vertex]) > len(self.graph[maxdegreeVertex]):
                maxdegreeVertex = vertex
        return maxdegreeVertex

    def log_approx(self):
        vertex_cover = []
        while self.numE > 0:
            maxdegreeVertex = self.getmaxdegree()
            vertex_cover.append(maxdegreeVertex)
            self.numE -= len(self.graph[maxdegreeVertex])
            self.numV -= 1
            self.remove_value(maxdegreeVertex)


        print("log-Approximation:", end="")
        for vertex in vertex_cover:
            print(" " + str(vertex), end="")



    def two_approx(self):
        vertex_cover = []
        while self.numE > 0:
            vertex1 = 0
            vertex2 = 0
            vertex1 = random.choice(list(self.graph))
            if len(self.graph[vertex1]) > 0:
                vertex_cover.append(vertex1)
                vertex2 = self.graph[vertex1][0]
                vertex_cover.append(vertex2)
                self.numE -= len(self.graph[vertex1])
                self.remove_value(vertex1)
                self.numV -= 1
                self.numE -= len(self.graph[vertex2])
                self.remove_value(vertex2)
                self.numV -= 1
            else:
                self.remove_value(vertex1)
                self.numV -= 1
        print("\n2-Approximation:", end="")
        for vertex in vertex_cover:
            print(" " + str(vertex), end="")

    def exact(self):
        valid_vertex_covers = []
        vertex_list = list(self.graph.keys())
        for i in range(1, self.numV + 1):
            perm_list = list(permutations(vertex_list, i))
            for perm in perm_list:
                G = copy.deepcopy(self)
                for num in perm:
                    G.numE -= len(G.graph[num])
                    G.remove_value(num)
                    G.numV -= 1
                if G.numE == 0:
                    valid_vertex_covers.append(perm)
                    break
            if len(valid_vertex_covers) == 1:
                break

        print("\nExact Solution:", end="")
        for vertex in min(valid_vertex_covers,key = len):
            print(" " + str(vertex), end="")

def main(argv):
    G1 = Graph()

    file = open(argv[1], "r")
    numVert = 0
    numEdge = 0

    edges = file.readline()
    while edges:
        edges = edges.strip()
        edge = edges.split(" ")
        G1.add_edge(int(edge[0]), int(edge[1]))
        G1.add_edge(int(edge[1]), int(edge[0]))
        numEdge += 1
        if int(edge[0]) > numVert:
            numVert = int(edge[0])
        if int(edge[1]) > numVert:
            numVert = int(edge[1])
        edges = file.readline()
    G1.numV = numVert + 1
    G1.numE = numEdge
    G2 = copy.deepcopy(G1)
    G3 = copy.deepcopy(G1)
    G1.log_approx()
    G2.two_approx()
    G3.exact()






if __name__ == "__main__":
    main(sys.argv)