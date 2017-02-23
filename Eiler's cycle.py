__author__ = 'student'
N = int(input())
M = int(input())
graph = [tuple(map(int, input().split())) for i in range(M)]
graph_matrix = [set() for s in range(N)]
for i in range(M):
    graph_matrix[graph[i][0]].add(graph[i][1])
    graph_matrix[graph[i][1]].add(graph[i][0])
def check_cycle(graph):
    order = [0 for i in range(N)]
    for i in range(N):
        order[i] = len(graph[i])
    if check_connectivity(0, graph, len(graph), set()):
        for i in order:
            if i % 2 != 0:
                return False
    else:
        return False
    return True

def check_connectivity(vertex, data, length, used = set()):
    used.add(vertex)
    for node in data[vertex]:
        if node not in used:
            check_connectivity(node, data, length, used)
    if len(used) == length:
         return True
if check_cycle(graph_matrix):
    print('YES')
else:
    print('NO')