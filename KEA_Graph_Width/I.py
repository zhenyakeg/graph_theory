class inser_text:
    pass
'''
В некотором государстве некотрые города соединены дорогами.
Жители этого государства просят вас помочь им с выбором столицы:
требуется, чтобы сумма расстояний от столицы до каждого из остальных городов была минимальна.
Для вашего удобства города уже пронумерованы от 0 до n-1 .
Формат входных данных
На вход программе в первой строке подается два числа через пробел:
n и m . n (2 <= n <= 100) - число городов, m (1 <= m <= 500) - число дорог.
В следующих m строках задаются дороги, по три числа в каждой строке - номера соединенных городов и длина дороги.
Формат выходных данных
Выведите номер столицы. Если возможно несколько варинтов, выведете любой.
'''

n, m = tuple(map(int, input().split()))
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
sum_dist_cities = {v:float('inf') for v in G}
for city in G:
    distances = dijkstra(G, city)
    sum_dist_cities[city] = sum(distances.values())
print(min(sum_dist_cities.items(),key= lambda x: x[1])[0])
