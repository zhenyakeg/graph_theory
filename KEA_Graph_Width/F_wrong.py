init_money = int(input())
row = list(map(int, input().split()))
G = {i:{} for i in range(len(row))}
for i in range(len(row)-2):
    G[i][i+2] = 1 + 0.01 * row[i+2]
    if i+3 < len(row):
        G[i][i+3] = 1 + 0.01 * row[i+3]

def dijkstra(G,start):
    global init_money
    d = {v: -1 for v in G}
    d[start] = init_money
    ways = {v: [] for v in G}
    ways[start].append(start)
    used = set()
    for i in range (len(d)):
        max_d = -1
        for v in d:
            if d[v] > max_d and v not in used:
                current = v
                max_d = d[v]
        for neighbour in G[current]:
            l = d[current] * G[current][neighbour]
            if l > d[neighbour]:
                d[neighbour] = l
                ways[neighbour] = ways[current] + [neighbour]
        used.add(current)
    return ways, d
result = dijkstra(G,0)
print(result)
print(*[i+1 for i in result[0][max(result[1].items(), key= lambda x: x[1])[0]]])