class task:

    task= '''Остовное дерево поиска в глубину. Реализация на Python 3.'''


def read_graph_as_lists():
    N, M = tuple(map(int,input().split()))
    graph = [[] for i in range(N)]
    for edge in range(M):
        a, b = tuple(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    return graph
def dfs(graph, start, path, used = None):
    if used == None:
        used = set()
    used.add(start)
    for vertex in graph[start]:
        if vertex not in used:
            path.append((start, vertex))
            dfs(graph, vertex, path, used)
def build_tree(graph):
    tree = []
    used = set()
    dfs(graph, 0, tree, used)
    return tree
for edge in build_tree(read_graph_as_lists()):
    print(*edge)



