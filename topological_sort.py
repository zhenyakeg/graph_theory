__author__ = 'student'
import sys
n, m = tuple(map(int,input().split()))
graph = [list() for i in range(n)]
for i in range (m):
    p, s = tuple(map(int, input().split()))
    graph[p].append(s)

def dfs(vertex, data, path, stack, used):
    used.add(vertex)
    stack.add(vertex)
    for node in data[vertex]:
        if node in stack:
            print('NO')
            sys.exit(0)
        if node not in used:
            dfs(node, data, path, stack, used)
    stack.remove(vertex)
    path.append(vertex)
def topological_sort(graph):
    global n
    path = []
    stack = set()
    used = set()
    for node in range(n):
        if node not in used:
            dfs(node, graph, path, stack, used)
    print(' '.join(map(str, path[::-1])))
topological_sort(graph)
