N, M = tuple(map(int, input().split()))
G = [[] for i in range(N)]
wm = [[float('inf')]*N for i in range(N)]
for j in range(M):
    a, b, c = tuple(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)
    wm[a][b] = c
    wm[b][a] = c
visited = [False] * N
path = []
paths = []
def all_hamilton(curr):
    global path, visited, G, paths, wm
    path.append(curr)
    visited[curr] = True
    if len(path) == N:
        if path[0] in G[path[-1]]:
            paths.append(path.copy())
    else:
        for next in G[curr]:
            if not visited[next]:
                all_hamilton(next)
    visited[curr] = False
    path.pop()
all_hamilton(0)
res_cost = float('inf')
res_path = []
for path in paths:
    curr_cost = 0
    for i in range(N):
        curr_cost += wm[path[i-1]][path[i]]
    if curr_cost < res_cost:
        res_cost = curr_cost
        res_path = path
print(res_cost)
print(*res_path)


