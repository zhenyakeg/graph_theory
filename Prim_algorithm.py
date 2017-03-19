N, M = tuple(map(int, input().split()))
G = [[] for i in range(N)]
for j in range(M):
    a, b, c = tuple(map(int, input().split()))
    G[a].append((b,c))
    G[b].append((a,c))

def prim(G):
    tree_edges = []
    tree_cost = 0
    tree_nodes = set()
    tree_nodes.add(0)
    for i in range (len(G) - 1):
        min_cost = float('inf')
        for vertex in tree_nodes:
            for (neighbour, cost) in G[vertex]:
                if neighbour not in tree_nodes and cost < min_cost:
                    min_cost = cost
                    current = neighbour
                    curr_edge = (vertex, neighbour)
        tree_cost += min_cost
        tree_edges.append(curr_edge)
        tree_nodes.add(current)
    return tree_cost, tree_edges

result = prim(G)
print(result[0])
for i in result[1]:
    print(*i)



