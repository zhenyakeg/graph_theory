from collections import defaultdict
def dfs_forward(vertex, data,  used, vector):
    used.add(vertex)
    for node in data.get(vertex, []):
        if node not in used:
            dfs_forward(node, data, used, vector)
    vector.append(vertex)
def dfs_back(vertex, data,  used):
    used.add(vertex)
    for node in data.get(vertex, []):
        if node not in used:
            dfs_back(node, data, used)
def weak_components(full_graph):
    counter = 0
    used = set()
    for i in full_graph.keys():
        if i not in used:
            dfs_back(i, full_graph, used)
            counter += 1
    return counter
N = int(input())
M = int(input())
graph = defaultdict(list)
inv_graph = defaultdict(list)
full_graph = defaultdict(list)

for i in range (M):
    a, b = tuple(map(int, input().split()))
    graph[a].append(b)
    inv_graph[b].append(a)
    full_graph[a].append(b)
    full_graph[b].append(a)

vector = list()
used = set()
counter = 0
for node in graph:
    if node not in used:
        dfs_forward(node, graph, used, vector)
used = set()
for i in range(len(vector)):
    vert = vector[len(vector) - 1 - i]
    if vert not in used:
        dfs_back(vert, inv_graph, used)
        counter += 1

print(weak_components(full_graph) + (N - len(full_graph)), counter + (N - len(vector)))
#не забыть добавить те, через который не прошел

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