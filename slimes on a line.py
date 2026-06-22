t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mn = a[0]
    mx = a[0]
    for i in range(1, n):
        if a[i] < mn:
            mn = a[i]
        if a[i] > mx:
            mx = a[i]
    print((mx - mn + 1) // 2)
