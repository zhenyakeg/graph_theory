import heapq

class Task:


    task= '''Алгоритм Дейкстры с восстановлением кратчайшего пути. Реализация на Python 3. Реализация для связного графа.
    Иначе просто пробегаем по компоненте связности, которую можно получить при помощи dfs или bfs. O(N^3)'''

def read_graph_as_lists():
    N, M = tuple(map(int, input().split()))
    graph = [[] for i in range(N)]
    for edge in range(M):
        a, b, c = tuple(map(int, input().split()))
        graph[a].append((b, c))
        graph[b].append((a, c))
    return graph


def dijkstra(graph, start, finish):
    distances = {v: float('inf') for v in graph}
    ways = {v: [] for v in graph}
    used = set()
    distances[start] = 0
    ways[start] = [start]
    while len(used) != len(graph):
        min_d = float('inf')
        for vertex in distances:
            if distances[vertex] < min_d and vertex not in used:
                min_d = distances[vertex]
                current_node = vertex

        for neighbour in graph[current_node]:
            l = distances[current_node] + graph[current_node][neighbour]
            if l < distances[neighbour]:
                distances[neighbour] = l
                ways[neighbour] = ways[current_node] + [neighbour]
        used.add(current_node)
    return distances[finish], ways[finish]


def dijkstra_heap(graph, start, finish):
    distances = [float('inf')] * len(graph)
    queue= []
    heapq.heappush(queue, (0, start))
    while queue:
        min_d, current_node = heapq.heappop(queue)
        if min_d > distances[current_node]:
            continue
        distances[current_node] = min_d
        for neighbour, cost in graph[current_node]:
            l = min_d + cost
            if l < distances[neighbour]:
                heapq.heappush(queue, (l, neighbour))
    return distances[finish]


start, finish = tuple(map(int, input().split()))
print(dijkstra_heap(read_graph_as_lists(), start, finish))
