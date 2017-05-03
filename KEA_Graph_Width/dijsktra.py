import heapq
class inser_text:
    pass
    """
    Дан взвешенный связный граф. Вершины пронумерованы от 0. Трeбуется с помощью алгоритма Дейкстры найти длину
    кратчайшего пути от вершины s до f.
    Формат входных данных
    На вход программе в первой строке подается четыре числа через пробел: n , m , s , f .
    Число n (2 <= n <= 1000) - число вершин в графе, m (1 <= m <= 20000) - число ребер.
     s и f - номера, соответственно, начальной и конечной вершин. В следующих m строках задаются ребра,
      по три числа в каждой строке - номера соединенных вершин и вес ребра.
    Формат выходных данных
    Длина кратчайшего пути между вершинами s и f.
    
    """
n, m, s, f = tuple(map(int, input().split()))
G = {i:{} for i in range(n)}
for i in range(m):
    b, e, c = tuple(map(int, input().split()))
    G[b][e] = c
    G[e][b] = c

def dijkstra(G,start):
    d = {v: float('inf') for v in G}
    d[start] = 0
    used = set()
    while len(used) != len(G):
        min_d = float('inf')
        for v in d:
            if d[v] < min_d and v not in used:
                current = v
                min_d = d[v]
        for neighbour in G[current]:
            l = d[current] + G[current][neighbour]
            if l < d[neighbour]:
                d[neighbour] = l
        used.add(current)
    return d
print(dijkstra(G,s)[f])