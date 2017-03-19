__author__ = 'student'
'''
 Ориентированный граф задан в формате списка рёбер. Проверить, является ли он сильно связным.
Формат входных данных

В первой строке вводится количество вершин N. Вершины без названий, их номера — 0, 1, 2 и т.д. до (N-1)-й включительно.

Во второй строке вводится количество рёбер M. Затем вводится M строк, содержащих по два числа через пробел — это номера
вершин, задающих ребро графа. Рёбра направленные .
Формат выходных данных

Одно слово YES, если орграф является сильно связным, или NO, если граф не сильно связный.
'''
N = int(input())
M = int(input())
graph = [set() for i in range(N)]
inv_graph = [set() for i in range(N)]
for i in range (M):
    a, b = tuple(map(int, input().split()))
    graph[a].add(b)
    inv_graph[b].add(a)
def dfs(vertex, data,  used):
    used.add(vertex)
    for node in data[vertex]:
        if node not in used:
            dfs(node, data, used)
    return used
def check_strong_connectivity(graph, inv_graph):
    if len(dfs(0,graph,set())) != len(graph) or  len(dfs(0,inv_graph,set())) != len(graph):
        return 'NO'
    else:
        return 'YES'
print(check_strong_connectivity(graph,inv_graph))