from collections import deque

def toQueen(x, y, p):
    global x_queen, y_queen, L, garden, N, M
    search_queue = deque()
    search_queue.append((x, y, 0))
    visited = []
    while search_queue:
        x_cur, y_cur, path = search_queue.popleft()
        if x_cur == x_queen and y_cur == y_queen:
            print(p)
            return p
        if path < L:
            path += 1
            if (x_cur, y_cur) not in visited:
                visited.append((x_cur, y_cur))
                if x_cur != 1 and garden[x_cur-2][y_cur-1] == '0':
                    search_queue.append((x_cur-1, y_cur, path))
                if x_cur != N and garden[x_cur][y_cur-1] == '0':
                    search_queue.append((x_cur+1, y_cur, path))
                if y_cur != 1 and garden[x_cur-1][y_cur-2] == '0':
                    search_queue.append((x_cur, y_cur-1, path))
                if y_cur != M and garden[x_cur-1][y_cur] == '0':
                    search_queue.append((x_cur, y_cur+1, path))
    return 0

with open('input.txt') as f:
    N, M = map(int, f.readline().split())
    garden = []
    for _ in range(N):
        garden.append(f.readline()[:M])
    x_queen, y_queen, L = map(int, f.readline().split())
    x_atos, y_atos, p_atos = map(int, f.readline().split())
    x_portos, y_portos, p_portos = map(int, f.readline().split())
    x_aramis, y_aramis, p_aramis = map(int, f.readline().split())
    x_dartan, y_dartan, p_dartan = map(int, f.readline().split())

result = toQueen(x_atos, y_atos, p_atos) + toQueen(x_portos, y_portos, p_portos)\
         + toQueen(x_aramis, y_aramis, p_aramis) + toQueen(x_dartan, y_dartan, p_dartan)
with open('output.txt', 'w') as f:
    f.write(str(result))
