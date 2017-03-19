class inser_text:
    pass
'''Найти кратчайший цикл
'''
n, m = tuple(map(int, input().split()))
graph = [[] for i in range(n)]
for i in range(m):
    xint, yint = tuple(map(int, input().split()))
    graph[xint].append(yint)

def distances(graph, start):
    used = set()
    used.add(start)
    dist = {start:0}
    Q = [start]
    way = {start:[start]}
    while Q:
        curr = Q.pop(0)
        for neighbour in graph[curr]:
            if neighbour not in used:
                used.add(neighbour)
                Q.append(neighbour)
                dist[neighbour] = dist[curr] + 1
                way[neighbour] = way[curr] + [neighbour]
    return dist, way

def find_min_cycle(graph):
    cycles = {}
    for vertex in range(len(graph)):
        curr_cycles = []
        for neighbbour in graph[vertex]:
            result = distances(graph, neighbbour)
            if vertex in result[1]:
                curr_cycles.append((neighbbour, result[0][vertex], result[1][vertex]))
            else:
                curr_cycles.append((neighbbour, float('inf'), None))
        if len(curr_cycles) == 0:
            cycles[vertex] = (float('inf'), None)
        else:
            tmp = min(curr_cycles, key= lambda x: x[1])
            cycles[vertex] = (tmp[1], tmp[2])
    answer = cycles[min(cycles, key= lambda x: cycles.get(x)[0])]
    if answer[1] == None:
        return ['NO CYCLES']
    else:
        return answer[1]
print(*find_min_cycle(graph))


