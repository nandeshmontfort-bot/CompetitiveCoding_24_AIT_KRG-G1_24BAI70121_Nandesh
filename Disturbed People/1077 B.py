n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(n - 2):
    if arr[i] == 1 and arr[i+1] == 0 and arr[i+2] == 1:
        count += 1
        arr[i+2] = 0 

print(count)
