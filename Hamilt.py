N, M = tuple(map(int, input().split()))
G = [[] for i in range(N)]
for j in range(M):
    a, b= tuple(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)

visited = [False] * N
way = []

def hamilton(curr):
    global way, visited, G
    way.append(curr)
    if len(way) == N:
        if way[0] in G[way[-1]]:
            return True
        else:
            way.pop()
            return False
    visited[curr] = True
    for next in range(N):
        if next in G[curr] and not visited[next]:
            if hamilton(next):
                return True
    visited[curr] = False
    way.pop()
    return False

hamilton(0)

print(*way)