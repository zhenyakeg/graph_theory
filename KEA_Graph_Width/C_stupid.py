n, m, st, fi = tuple(map(int, input().split()))
graph = [list() for i in range(n)]

for i in range (m):
    a, b = tuple(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def distances(graph, start):
    used = set()
    used.add(start)
    dist = {start:0}
    Q = [start]
    while Q:
        curr = Q.pop(0)
        for neighbour in graph[curr]:
            if neighbour not in used:
                used.add(neighbour)
                Q.append(neighbour)
                dist[neighbour] = dist[curr] + 1
    return dist

dist_graph = distances(graph,st)

print(dist_graph[fi])