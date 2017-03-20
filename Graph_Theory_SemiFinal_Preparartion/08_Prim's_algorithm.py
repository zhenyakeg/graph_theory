class task:

    task= '''Алгоритм построения минимального остовного дерева. Алгоритм Прима на неориентированном взвешенном связном графе'''

def read_as_lists():
    N, M = tuple(map(int, input()))
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b, c = tuple(map(int, input().split()))
        graph[a].append((b, c))
        graph[b].append((a, c))
    return graph
def prim(graph_as_lists, start_point):
    costs = [float('inf') for i in range(len(graph_as_lists))] #матрица стоимостей добавления вершины к каркасу
    costs[start_point] = 0
    tree_nodes = [start_point]
    tree_edges = []
    tree_weight = 0
    for i in range(len(graph_as_lists) - 1):
        curr_min_cost = float('inf')
        for vertex in tree_nodes:
            for (neighbour, price) in graph_as_lists[vertex]:
                if neighbour not in tree_nodes and price < curr_min_cost:
                    curr_node = neighbour
                    curr_min_cost = price
                    curr_edge = (vertex, neighbour)
        tree_nodes.append(curr_node)
        tree_edges.append(curr_edge)
        tree_weight += curr_min_cost
        return tree_weight, tree_edges

