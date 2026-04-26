import sys
input = sys.stdin.readline

n = int(input())
edges = []
deg = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))
    deg[u] += 1
    deg[v] += 1

special = -1
for i in range(1, n + 1):
    if deg[i] >= 3:
        special = i
        break

res = [-1] * (n - 1)
cur = 0
if special != -1:
    for i in range(n - 1):
        u, v = edges[i]
        if u == special or v == special:
            if cur < 3:
                res[i] = cur
                cur += 1

for i in range(n - 1):
    if res[i] == -1:
        res[i] = cur
        cur += 1

for x in res:
    print(x)
