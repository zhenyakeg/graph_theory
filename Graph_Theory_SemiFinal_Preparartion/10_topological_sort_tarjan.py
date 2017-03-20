import sys
class task:

    task = '''Топологическая сортировка. Алгоритм Кана и Тарьяна. Реализация одного из них на Python 3.'''


def read_graph_as_lists():
    N, M = tuple(map(int, input().split()))
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = tuple(map(int, input().split()))
        graph[a].append(b)
    return graph


def dfs_with_stack(graph, start, path, stack=None, used=None):
    if stack == None:
        stack = set()
    if used == None:
        used = set()
    stack.add(start)
    used.add(start)
    for neighbour in graph[start]:
        if neighbour in stack:
            print('Not acyclic. Sorting Impossible.')
            sys.exit(0)
        if neighbour not in used:
            dfs_with_stack(graph, neighbour, path, stack, used)
        path.append(start)
        stack.remove(start)


def tarjan_topological_sort(graph):
    sorted_graph = []
    used = set()
    stack = set()
    for node in range(len(graph)):
        if node not in used:
            dfs_with_stack(graph, node, sorted_graph, stack, used)

    return sorted_graph
