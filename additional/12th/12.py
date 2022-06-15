inp = open("input.txt")

c_rooms, c_ribs = map(int, inp.readline().split())

maze = [{} for _ in range(c_rooms)]
for _ in range(c_ribs):
    src, dst, color = map(int, inp.readline().split())
    maze[src - 1][color - 1] = dst - 1
    maze[dst - 1][color - 1] = src - 1

c_moves = int(inp.readline())
moves = list(map(int, inp.readline().split()))

inp.close()

curr = 0
fail = False
for i in range(c_moves):
    move_color = moves[i] - 1
    if(move_color not in maze[curr].keys()):
        fail = True
        break
    new = maze[curr][move_color]
    if (new is not None):
        curr = new
    else:
        fail = True
        break

out = open("output.txt", "w")
if(fail):
    out.write("INCORRECT")
else:
    out.write(str(curr + 1))
out.close()

