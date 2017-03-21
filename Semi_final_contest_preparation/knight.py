def rename_straight(point):
    alphabet = []
    for letter in 'abcdefgh':
        alphabet.append(letter)
    nums = list(range(1, 9))
    renaming_dict = dict(zip(alphabet, nums))
    return (renaming_dict[point[0]], int(point[1]))
def rename_back(point):
    alphabet = []
    for letter in 'abcdefgh':
        alphabet. append(letter)
    nums = list(range(1, 9))
    renaming_dict = dict(zip(nums, alphabet))
    return renaming_dict[point[0]] + str(point[1])
def check_out(point):
    if point[0] > 8 or point[0] < 1 or point[1] > 8 or point[1] < 1:
        return False
    return True
def build_graph():
    moves = {(i, j): [] for i in range(1, 9) for j in range(1, 9)}
    for i in range(1, 9):
        for j in range(1,9):
            for (di, dj) in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
                if check_out((i + di, j + dj)):
                    moves[(i, j)].append((i + di, j + dj))
    return moves
def bfs(graph, start, finish):
    used = set()
    Q = [start]
    dist = {v: float('inf') for v in graph}
    paths = {v: [] for v in graph}
    dist[start] = 0
    paths[start] = [start]
    while Q:
        current = Q.pop(0)
        for neighbour in graph[current]:
            if neighbour not in used:
                Q.append(neighbour)
                used.add(neighbour)
                dist[neighbour] = dist[current] + 1
                paths[neighbour] = paths[current] + [neighbour]
    return paths[finish]
start = rename_straight(input())
finish = rename_straight(input())
result = list(map(rename_back, bfs(build_graph(), start, finish)))
for move in result:
    print(move)