__author__ = 'student'
def matrix_list():
    N = int(input())
    graph_matrix = [[None]*N for i in range(N)]
    for i in range(N):
        graph_matrix[i] = list(map(int, input().split()))
    graph_list = []
    for i in range(N):
        for j in range(N):
            if graph_matrix[i][j]:
                graph_list.append([i , j, graph_matrix[i][j]])
    return graph_list
out = matrix_list()
for i in range(len(out)):
    print(*out[i])
