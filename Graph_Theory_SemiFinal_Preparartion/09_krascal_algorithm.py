def read_as_edges_list():
    N, M = tuple(map(int, input().split()))
    edges = []
    for i in range(M):
        edges.append(tuple(map(int, input().split())))
    return edges, N
def krascal(graph_as_edges, num_of_vertexes):
    tree = []
    tree_weight = 0
    edges = sorted(graph_as_edges, key=lambda x: x[2])
    names_of_components = [i for i in range(num_of_vertexes)] # имена компонент связности.
    for vertex1, vertex2, cost in edges:
        if names_of_components[vertex1] != names_of_components[vertex2]:
            tree.append((vertex1, vertex2))
            tree_weight += cost
        for i in range(num_of_vertexes):
            if names_of_components[i] == names_of_components[vertex2]:
                names_of_components[i] = names_of_components[vertex1]
    return tree_weight, tree