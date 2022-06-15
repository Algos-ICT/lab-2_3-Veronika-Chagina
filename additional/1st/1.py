inp = open("input.txt")

c_nodes, c_ribs = map(int, inp.readline().split())

links = [[] for _ in range(c_nodes)]

for _ in range(c_ribs):
    node, link = map(int, inp.readline().split())
    links[node-1].append(link-1)
    links[link-1].append(node-1)

start, target = map(int, inp.readline().split())

start -= 1
target -=1

inp.close()

visited = [False] * c_nodes
que = [start]

exist = False
visited[start] = True
while(len(que) > 0):
    node = que.pop()
    if(node == target):
        exist = True
        break
    for j in links[node]:
        if(not visited[j]):
            que.append(j)
            visited[j] = True

out = open("output.txt", "w")
if(exist):
    print("1")
    out.write("1")
else:
    print("0")
    out.write("0")
out.close()