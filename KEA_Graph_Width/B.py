__author__ = 'student'

n, m = tuple(map(int, input().split()))
graph = [list() for i in range(n)]
for i in range (m):
    a, b = tuple(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def tree(graph, start):
    used = set()
    used.add(start)
    Q = [start]
    while Q:
        curr = Q.pop(0)
        for neighbour in graph[curr]:
            if neighbour not in used:
                used.add(neighbour)
                Q.append(neighbour)
                print(curr, neighbour)

tree(graph, 0)