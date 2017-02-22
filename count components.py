__author__ = 'student'
N = int(input())
M = int(input())
graph = [tuple(map(int, input().split())) for i in range(M)]
graph_matrix = [set() for i in range (N)]
for i in range(M):
    graph_matrix[graph[i][0]].add(graph[i][1])
    graph_matrix[graph[i][1]].add(graph[i][0])

count = 0
_used = set()
def dfs(vertex, data,  used):
    used.add(vertex)
    for node in data[vertex]:
        if node not in used:
            dfs(node, data, used)
for i in range(N):
    if i not in _used:
        dfs(i, graph_matrix, _used)
        count += 1
print(count)
