N, M = tuple(map(int, input().split()))
G = [[] for i in range(N)]
for j in range(M):
    a, b= tuple(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)
visited = [False] * N
path = []
def hamilton(curr):
    global path, visited, G
    path.append(curr)
    if len(path) == N:
        if path[0] in G[path[-1]]:
            return True
        else:
            path.pop()
            return False
    visited[curr] = True
    for next in range(N):
        if next in G[curr] and not visited[next]:
            if hamilton(next):
                return True
    visited[curr] = False
    path.pop()
    return False
hamilton(0)

print(*path)