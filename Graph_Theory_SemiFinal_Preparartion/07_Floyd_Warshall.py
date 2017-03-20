class task:

    task= '''Алгоритм Флойда-Уоршелла для поиска кратчайшего пути от одной вершины до другой.
    В основе- динамическое програмирование. Асимптотика O(N^3) Реализация на Python 3.'''

def read_as_weight_matrix():
    N, M = tuple(map(int, input()))
    wm = [[float('+inf') for i in range(N)] for i in range(N)]
    for i in range(M):
        a, b, c = tuple(map(int, input().split()))
        wm[a][b] = c
    return wm
def floyd_warshall(graph_as_wm):
    A = [[[float('inf') for i in range(len(graph_as_wm))] for j in range(len(graph_as_wm))] for k in range(len(graph_as_wm) + 1)]
    A[0] = graph_as_wm.copy()
    for k in range(1, len(graph_as_wm) + 1):
        for i in range(len(graph_as_wm)):
            for j in range(len(graph_as_wm)):
                A[k][i][j] = min(A[k-1][i][j], A[k - 1][i][k] + A[k-1][k][j])
    return A[len(graph_as_wm)]

