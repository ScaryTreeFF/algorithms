from collections import defaultdict
import Heap
import random
import timeit
'''
Вариант d=1, …, 10
А - алгоритм Дейкстры, реализованный на основе (d+1)–кучи,
В - алгоритм Дейкстры, реализованный на основе (d+2)–кучи;

    3. Провести эксперименты на основе следующих данных:
        3.1.  n = 100, … ,104 с шагом 100, q = 1, r =106, количество ребер:
        а) m ≈ n2/10, б) m ≈ n2/2 (нарисовать графики функций TА(n) и ТВ(n) для обоих случаев);
'''


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


def Dijkstra(edges, start, d):
    begin = timeit.default_timer()

    A = [None] * len(edges)
    queue = Heap.Heap(d)
    queue.insert((0, start))
    while queue.size != 0:
        path_len, v = queue.pop()
        if A[v] is None:  # v is unvisited
            A[v] = path_len
            for w, edge_len in edges[v].items():
                if A[w] is None:
                    queue.insert((path_len + edge_len, w))

    # to give same result as original, assign zero distance to unreachable vertices
    # return [0 if x is None else x for x in A]
    end = timeit.default_timer()
    return (end - begin)


def invert_graph_to_edges(graph):
    edges = defaultdict(dict)
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if (graph[i][j] != 0):
                edges[i][j] = graph[i][j]

    return edges


q = 1
r = 10 ** 6

with open('time_binary-a.txt', 'w') as file1:
    with open('time_ternary-a.txt', 'w') as file2:
        for n in range(100, 10001, 100):
            m = int(n ** 2 / 10)

            G = newGraph(n, m, q, r)

            time_binary = Dijkstra(invert_graph_to_edges(G), 0, 2)
            time_ternary = Dijkstra(invert_graph_to_edges(G), 0, 3)

            file1.write(str(time_binary) + ' ')
            file2.write(str(time_ternary) + ' ')

            print("n : {}\t m : {}\t time_binary : {}\t time_ternary : {}".format(
                    n, m, time_binary, time_ternary))
