class task:
    task= '''Считывание матрицы смежности орграфа и вывод списков смежности. Начальный граф задан списком ребер,
    с изначальным заданием их числа и числа вершин'''
def read_graph_as_matrix():
    N, M = tuple(map(int, input().split()))
    graph = [[0 for j in range(N)] for i in range(N)]
    for edge in range(M):
        a, b = tuple(map(int, input().split()))
        graph[a][b] = 1
    return graph
def print_graph_as_lists(graph_as_matrix):
    graph_as_lists = [[] for i in range(len(graph_as_matrix))]
    for vertex1 in range(len(graph_as_matrix)):
        for vertex2 in range(len(graph_as_matrix)):
            if graph_as_matrix[vertex1][vertex2] == 1:
                graph_as_lists[vertex1].append(vertex2)
    for i in range(len(graph_as_lists)):
        print(i,':',' '.join(map(str, graph_as_lists[i])))
print_graph_as_lists(read_graph_as_matrix())