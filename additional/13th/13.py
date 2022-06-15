inp = open("input.txt")

c_rows, c_cols = map(int, inp.readline().split())

links = [[] for _ in range(c_rows * c_cols)]

field = []
line = inp.readline()
for col in range(1, c_cols):
    if(line[col] == "#"):
        if(line[col - 1] == "#"):
            links[col - 1].append(col)
            links[col].append(col - 1)
field.append(line)

for row in range(1, c_rows):
    line = inp.readline()
    field.append(line)
    for col in range(0, c_cols):
        if(field[row][col] == "#"):
            if(col == 0):
                if(field[row - 1][col] == "#"):
                    links[row * c_cols + col].append((row - 1) * c_cols + col)
                    links[(row - 1) * c_cols + col].append(row * c_cols + col)
            else:
                if(field[row][col - 1] == "#"):
                    links[row * c_cols + col].append(row * c_cols + col - 1)
                    links[row * c_cols + col - 1].append(row * c_cols + col)
                if(field[row - 1][col] == "#"):
                    links[row * c_cols + col].append((row - 1) * c_cols + col)
                    links[(row - 1) * c_cols + col].append(row * c_cols + col)

inp.close()


used = [False] * (c_rows * c_cols)
c_areas = 0

for row in range(c_rows):
    for col in range(c_cols):
        enter = False
        if(not used[row * c_cols + col]):
            que = [row * c_cols + col]
            used[row * c_cols + col] = True
            if(field[row][col] == "#"):
                enter = True
            while(len(que) > 0):
                node = que.pop()
                for j in links[node]:
                    enter = True
                    if(not used[j]):
                        que.append(j)
                        used[j] = True
        if(enter):
            c_areas += 1
    
out = open("output.txt", "w")
out.write(str(c_areas))
out.close()
    