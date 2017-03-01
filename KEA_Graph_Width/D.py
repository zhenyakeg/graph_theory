__author__ = 'student'

size = tuple(map(int,input().split()))
start = tuple(map(int,input().split()))
finish = tuple(map(int,input().split()))
field = [[1 for i in range(size[1])] for j in range(size[0] + 2)]

for p in range (size[0]):
    row = input()
    for j in range(len(row)):
        if row[j] == 'X':
            field[p][j] = 1
        elif row[j] == ' ':
            field[p][j] = 0

def generate_graph(field, size):
    graph = [[] for i in range(size[0]*size[1])]
    for p in range(size[0]):
        for s in range(size[1]):
            if field[p][s] == 0:
                if p + 1 < size[0] and field[p + 1][s] == 0:
                    graph[(p)*size[1] + s]. append((p+1)*size[1] + s)
                if s + 1 < size[1] and field[p][s + 1] == 0:
                    graph[(p)*size[1] + s]. append((p)*size[1] + s + 1)
                if p - 1 >= 0 and field[p - 1][s] == 0:
                    graph[(p)*size[1] + s]. append((p-1)*size[1] + s)
                if s - 1 >= 0 and field[p][s - 1] == 0:
                    graph[(p)*size[1] + s]. append((p)*size[1] + s - 1)
    return graph

def get_num(point):
    global size
    return (point[0])*size[1] + point[1]

def count_way(graph, start, finish):
    global size
    used = set()
    used.add(get_num(start))
    dist = {get_num(start):0}
    Q = [get_num(start)]
    while Q:
        curr = Q.pop(0)

        for neighbour in graph[curr]:
            if neighbour not in used:
                if neighbour == get_num(finish):
                    return dist[curr] + 1
                used.add(neighbour)
                Q.append(neighbour)
                dist[neighbour] = dist[curr] + 1
    return 'INF'

print(count_way(generate_graph(field, size), start, finish))
