__author__ = 'student'
'''
 Дан невзвешенный неориентированный связный граф. Вершины пронумерованы от 0. Трeбуется с помощью обхода в ширину найти расстояния от 0-й до всех остальных вершин.
Формат входных данных

На вход программе в первой строке подаются через пробел два числа: n (2 <= n <= 1000) — число вершин в графе и m (1 <= m <= 20000) — число рёбер.
В следующих m строках задаются ребра: по два числа в каждой строке — номера соединённых вершин.
Формат выходных данных

Требуется распечатать n чисел, каждое на новой строке. В первой строке — расстояния от 0-й вершины до 0-й, во второй - от 0-й до 1-й, в третьей — от 0-й до 2-й и т.д.
'''
n, m = tuple(map(int, input().split()))
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

dist_graph = distances(graph,0)

for i in range(n):
    print(dist_graph[i])


