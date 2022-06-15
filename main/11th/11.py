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
            if cur_node in sides:
                for node in sides[cur_node]:
                    search_queue.append((node, path))
    return -1

with open('input.txt') as f:
    m = int(f.readline())
    sides = {}
    for i in range(m):
        v1, sign, v2 = map(str, f.readline().split())
        if v1 in sides:
            sides[v1].append(v2)
        else:
            sides[v1] = [v2]
    u = f.readline()[:-1]
    v = f.readline()[:-1]

result = shortPath(u, v)
with open('output.txt', 'w') as f:
    f.write(str(result))