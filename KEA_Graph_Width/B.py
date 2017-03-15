__author__ = 'student'
'''Дан невзвешенный неориентированный связный граф. Вершины пронумерованы от 0.
Трeбуется с помощью обхода в ширину построить остовное дерево.
Формат входных данных
На вход программе в первой строке подаются через пробел два числа:
n (2 <= n <= 1000) — число вершин в графе и m (1 <= m <= 20000) — число рёбер. В следующих m строках задаются ребра:
 по два числа в каждой строке — номера соединённых вершин.
Формат выходных данных
Требуется распечатать n-1 пару чисел, каждyю на новой строке. Каждая пара задаёт ребро в остовном дереве.'''


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