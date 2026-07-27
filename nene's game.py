t = int(input())
for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    n = list(map(int, input().split()))
    x = a[0]   
    for i in n:
        if i < x:
            print(i, end=" ")
        else:
            print(x - 1, end=" ")
    print()
