class task:

    task= '''Подсчёт компонент связности поиском в глубину. Реализация на Python 3. O(N*NUM_comp)'''


def read_graph_as_lists():
    N, M = tuple(map(int,input().split()))
    graph = [[] for i in range(N)]
    for edge in range(M):
        a, b = tuple(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    return graph
def dfs(graph, start, used = None):
    if used == None:
        used = set()
    used.add(start)
    for vertex in graph[start]:
        if vertex not in used:
            dfs(graph, vertex, used)
def count_components(graph):
    used = set()
    number_of_components = 0
    for vertex in range(len(graph)):
        if vertex not in used:
            dfs(graph, vertex, used)
            number_of_components += 1
    return number_of_components

print(count_components(read_graph_as_lists()))

