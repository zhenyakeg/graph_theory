class inser_text:
    pass
"""Кратчайший путь от a к b
"""
n, m, a, b = tuple(map(int,input().split()))
graph = [list() for i in range(n)]

for i in range (m):
    p, s = tuple(map(int, input().split()))
    graph[p].append(s)
    graph[s].append(p)

def bfs_doubled(graph, start, finish):
    used1 = set()
    used2 = set()
    used1.add(start)
    used2.add(finish)
    dist1 = {start:0}
    dist2 = {finish:0}
    Q1 = [start]
    Q2 = [finish]
    while Q1 and Q2:
        curr1 = Q1.pop(0)
        curr2 = Q2.pop(0)
        for neighbour1 in graph[curr1]:
            if neighbour1 not in used1:
                used1.add(neighbour1)
                Q1.append(neighbour1)
                dist1[neighbour1] = dist1[curr1] + 1
        for neighbour2 in graph[curr2]:
            if neighbour2 not in used2:
                used2.add(neighbour2)
                Q2.append(neighbour2)
                dist2[neighbour2] = dist2[curr2] + 1
        if curr1 in used2:
            return dist2[curr1] + dist1[curr1]
        if curr2 in used1:
            return dist1[curr2] + dist2[curr2]
print (bfs_doubled(graph, a, b))

'''16 17 0 15
0 1
1 2
0 3
0 4
0 5
5 6
5 7
5 8
5 15
15 14
15 13
15 12
15 11
8 9
8 10
10 11
11 12'''