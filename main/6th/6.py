from collections import deque


def shortPath(u, v):
    global sides
    search_queue = deque()
    search_queue.append((u, 0))
    visited = []
    while search_queue:
        cur_node, path = search_queue.popleft()
        if cur_node == v:
            return path
        path += 1
        if cur_node not in visited:
            visited.append(cur_node)
            for node in sides[cur_node]:
                search_queue.append((node, path))
    return -1


with open('input.txt') as f:
    n, m = map(int, f.readline().split())
    sides = {}
    for i in range(n+1):
        sides[i] = []
    for i in range(m):
        v1, v2 = map(int, f.readline().split())
        sides[v1].append(v2)
        sides[v2].append(v1)
    u, v = map(int, f.readline().split())

result = shortPath(u, v)
print(result)
