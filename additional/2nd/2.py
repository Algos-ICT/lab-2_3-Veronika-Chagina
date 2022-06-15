inp = open("input.txt")

c_nodes, c_ribs = map(int, inp.readline().split())

links = [[] for _ in range(c_nodes)]

for _ in range(c_ribs):
    node, link = map(int, inp.readline().split())
    links[node-1].append(link-1)
    links[link-1].append(node-1)

inp.close()

visited = [False] * c_nodes
c_areas = 0

for i in range(c_nodes):
    if(not visited[i]):
        c_areas += 1
        que = [i]
        visited[i] = True
        while(len(que) > 0):
            node = que.pop()
            for j in links[node]:
                if(not visited[j]):
                    que.append(j)
                    visited[j] = True

print(c_areas)

out = open("output.txt", "w")
out.write(str(c_areas))
out.close()
