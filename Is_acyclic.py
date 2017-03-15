__author__ = 'student'
import sys
n, m = tuple(map(int,input().split()))
graph = [list() for i in range(n)]

for i in range (m):
    p, s = tuple(map(int, input().split()))
    graph[p].append(s)
def dfs(vertex, data, path, used):
    if used == None:
        used = set()
    if path == None:
        path = []
    used.add(vertex)
    path.append(vertex)
    for node in data[vertex]:
        if node == path[0]:
            print(" ".join(map(str,path)))
            sys.exit(0)
        if node not in used:
            dfs(node, data, path, used)
    path.pop()
def is_acyclic(graph):
    for node in range(len(graph)):
        stack = []
        used = set()
        dfs(node, graph, stack, used)
    print('YES')
is_acyclic(graph)
