t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        nums = []
        
        for i in range(1, n*n + 1, 2):
            nums.append(i)
        
        for i in range(2, n*n + 1, 2):
            nums.append(i)
        
        idx = 0
        for i in range(n):
            print(*nums[idx:idx+n])
            idx += n
