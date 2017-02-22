__author__ = 'student'
N = int(input())
M = int(input())
graph = [tuple(map(int, input().split())) for i in range(M)]
graph_matrix = [set() for i in range (N)]
for i in range(M):
    graph_matrix[graph[i][0]].add(graph[i][1])
    graph_matrix[graph[i][1]].add(graph[i][0])
order = [0 for i in range(N)]
for i in range(N):
    order[i] = len(graph_matrix[i])

