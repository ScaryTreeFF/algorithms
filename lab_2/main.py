import sys


def MSP_PRIM(n, graph):
    used = [False for i in range(n)]
    min_e = [sys.maxsize for i in range(n)]
    sel_e = [-1 for i in range(n)]
    min_e[0] = 0

    for i in range(n):
        v = -1
        for j in range(n):
            if (not used[j] and (v == -1 or min_e[j] < min_e[v])):
                v = j

        if (min_e[v] == sys.maxsize):
            print("No MST")
            sys.exit()

        used[v] = True
        if (sel_e[v] != -1):
            print("{} {}".format(v, sel_e[v]))

        for to in range(n):
            if (graph[v][to] < min_e[to] and graph[v][to] != 0):
                min_e[to] = graph[v][to]
                sel_e[to] = v


def MSP_KRUSKAL(n, edges):      # edges = [(weight, start, end), ...]
    edges.sort()
    comp = [i for i in range(n)]
    for weight, start, end in edges:
        if comp[start] != comp[end]:
            print("{} {}".format(start, end))
            a = comp[start]
            b = comp[end]
            for i in range(n):
                if comp[i] == b:
                    comp[i] = a


def invert_graph_to_edges(n, graph):
    edges = []
    for i in range(n):
        for j in range(i, n):
            if (graph[i][j] != 0):
                edges.append((graph[i][j], i, j))
    return edges


graph1 = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
        ]

graph2 = [
        [0, 3, 1, 6, 0, 0],
        [3, 0, 5, 0, 3, 0],
        [1, 5, 0, 5, 6, 4],
        [6, 0, 5, 0, 0, 2],
        [0, 3, 6, 0, 0, 6],
        [0, 0, 4, 2, 6, 0],
        ]

# MSP_PRIM(6, graph2)
print("============")
MSP_KRUSKAL(6, invert_graph_to_edges(graph2))