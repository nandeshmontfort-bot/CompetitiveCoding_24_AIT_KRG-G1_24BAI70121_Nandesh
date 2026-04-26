t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    
    for x in arr:
        if x == 1:
            count += 1
        else:
            break
    
    if count == n:
        if count % 2 == 1:
            print("First")
        else:
            print("Second")
    else:
        if count % 2 == 0:
            print("First")
        else:
            print("Second")
