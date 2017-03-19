class task:

    task= '''Остовное дерево поиска в ширину. Реализация на Python 3.'''

def read_graph_as_lists():
    N, M = tuple(map(int,input().split()))
    graph = [[] for i in range(N)]
    for edge in range(M):
        a, b = tuple(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    return graph
def bfs(graph, start, path, used = None):
    if used == None:
        used = set()
    used.add(start)
    Q = [start]
    while Q:
        vertex = Q.pop()
        for neighbour in graph[vertex]:
            if neighbour not in used:
                path.append((vertex, neighbour))
                used.add(neighbour)
                Q.append(neighbour)
    return path


def build_tree(graph):
    tree = []
    used = set()
    bfs(graph, 0, tree, used)
    return tree
for edge in build_tree(read_graph_as_lists()):
    print(*edge)