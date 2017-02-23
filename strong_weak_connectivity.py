N = int(input())
M = int(input())
graph = [set() for i in range(N)]
inv_graph = [set() for i in range(N)]
full_graph = [set() for i in range(N)]
for i in range (M):
    a, b = tuple(map(int, input().split()))
    graph[a].add(b)
    inv_graph[b].add(a)
    full_graph[a].add(b)
    full_graph[b].add(a)

def dfs(vertex, data,  used):
    used.add(vertex)
    for node in data[vertex]:
        if node not in used:
            dfs(node, data, used)

def kesaraiu(graph, inv_graph):
    counter = []
    i = 0
    while i < len(graph):
        stack = set()
        inv_stack = set()
        dfs(i, graph, stack)
        dfs(i, inv_graph, inv_stack)
        if (stack & inv_stack) not in counter:
            counter.append(stack & inv_stack)
        i += len(stack & inv_stack)
    return len(counter)

def weak_components(full_graph):
    counter = 0
    used = set()
    for i in range(len(full_graph)):
        if i not in used:
            dfs(i, full_graph, used)
            counter += 1
    return counter

print(weak_components(full_graph), kesaraiu(graph,inv_graph))

'''11
13
0 1
1 2
2 0
1 3
3 4
4 5
5 3
6 5
6 7
7 8
8 9
9 6
10 9
1 4
'''