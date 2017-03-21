first = list(map(int, input().split()))
n, m = first[0], first[1]
main_cities = first[2::]
graph = {i: {} for i in range(n)}
for i in range(m):
    a, b, c = tuple(map(int, input().split()))
    graph[a][b] = c
    graph[b][a] = c
def dfs(graph, start, used= None):
    if used is None:
        used = set()
    used.add(start)
    for neighbour in graph[start]:
        if neighbour not in used:
            dfs(graph, neighbour, used)
    return used

def dijkstra(graph, start, finish):
    distances = {v: float('inf') for v in graph}
    ways = {v: [] for v in graph}
    used = set()
    distances[start] = 0
    # ways[start] = [start]
    component = dfs(graph, start)
    if finish not in component:
        return float('inf')
    else:
        while len(used) != len(component):
            min_d = float('inf')
            for vertex in distances:
                if distances[vertex] < min_d and vertex not in used:
                    min_d = distances[vertex]
                    current_node = vertex
            for neighbour in graph[current_node]:
                l = distances[current_node] + graph[current_node][neighbour]
                if l < distances[neighbour]:
                    distances[neighbour] = l
                    # ways[neighbour] = ways[current_node] + [neighbour]
            used.add(current_node)
        return distances[finish] #, ways[finish]
districts = {c: {m: float('inf') for m in main_cities} for c in range(n)}
for city in graph:
    for main_city in main_cities:
        districts[city][main_city] = dijkstra(graph, city, main_city)
for i in range(n):
    res = min(districts[i].items(), key= lambda x: x[1])
    if res[1] == float('inf'):
        print(-1)
    else:
        print(res[0])
