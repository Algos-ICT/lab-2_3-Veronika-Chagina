import math

inp = open("input.txt")

c_villages = int(inp.readline())
start, end = map(int, inp.readline().split())
c_races = int(inp.readline())

buses = [[] for _ in range(c_races)]

for _ in range(c_races):
    src, src_time, dst, dst_time = map(int, inp.readline().split())
    buses[src - 1].append((src_time, dst - 1, dst_time))

times = [math.inf] * (c_villages)
times[start - 1] = 0

used = [False] * (c_villages)
while True:
    min_time = math.inf
    for i in range(c_villages):
        if not used[i] and times[i] < min_time:
            min_time = times[i]
            min_village = i
    if min_time == math.inf:
        break
    src = min_village
    used[src] = True
    for src_time, dst, dst_time in buses[src]:
        if times[src] <= src_time and dst_time < times[dst]:
            times[dst] = dst_time

out = open("output.txt", "w")
if times[end - 1] == math.inf:
    out.write("-1")
else:
    out.write(str(times[end - 1]))
