n = int(input())
arr = list(map(int, input().split()))

total_ones = sum(arr)

gain = []
for x in arr:
    if x == 0:
        gain.append(1)
    else:
        gain.append(-1)

max_gain = gain[0]
current = gain[0]

for i in range(1, n):
    current = max(gain[i], current + gain[i])
    max_gain = max(max_gain, current)

print(total_ones + max_gain)
