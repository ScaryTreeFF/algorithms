import sys
import random
import timeit


# Generates a graph with n vertices and m edges
def newGraph(n: int, m: int, q: int, r: int):
    if n < 2:
        raise ValueError

    if m > (n * (n - 1) / 2):
        raise ValueError

    if m < n - 1:
        raise ValueError

    generator = random.SystemRandom()

    graph = [[0 for x in range(0, n)] for y in range(0, n)]
    for i in range(0, n - 1):
        graph[i][i + 1] = graph[i + 1][i] = generator.randint(q, r)

    for i in range(0, m - n + 1):
        a = b = 0
        while True:
            a = generator.randint(0, n - 1)
            b = generator.randint(0, n - 1)
            if ((a > b + 1 or a < b - 1) and graph[a][b] == 0):
                break
        graph[a][b] = graph[b][a] = generator.randint(q, r)

    return graph


def MSP_PRIM(n, graph):
    begin = timeit.default_timer()

    MSP = []
    used = [False for i in range(n)]         # visited vertices
    min_e = [sys.maxsize for i in range(n)]  # min distance from curr vertice to others
    sel_e = [-1 for i in range(n)]           # second part of the edge
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
            MSP.append((v, sel_e[v]))

        for to in range(n):
            if (graph[v][to] < min_e[to] and graph[v][to] != 0):
                min_e[to] = graph[v][to]
                sel_e[to] = v

        end = timeit.default_timer()
        return (end - begin)  # return elapsed time in seconds


def MSP_KRUSKAL(n, edges):      # edges = [(weight, start, end), ...]
    begin = timeit.default_timer()

    MSP = []
    edges.sort()
    comp = [i for i in range(n)]
    for weight, start, end in edges:
        if comp[start] != comp[end]:
            MSP.append((start, end))
            a = comp[start]
            b = comp[end]
            for i in range(n):
                if comp[i] == b:
                    comp[i] = a

    end = timeit.default_timer()
    return (end - begin)


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
q = 1
r = 10 ** 6


with open('time_prim.txt', 'w') as file1:
    with open('time_kruskal.txt', 'w') as file2:
        for n in range(100, 10001, 100):
            m = int(n ** 2 / 10)

            G = newGraph(n, m, q, r)

            time_prim = MSP_PRIM(n, G)
            time_kruskal = MSP_KRUSKAL(n, invert_graph_to_edges(n, G))

            file1.write(str(time_prim) + ' ')
            file2.write(str(time_kruskal) + ' ')

            print("n : {}\t m : {}\t time_prim : {}\t time_kruskal : {}".format(
                    n, m, time_prim, time_kruskal))
