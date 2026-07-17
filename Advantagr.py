t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    temp = sorted(arr)
    first = temp[-1]
    second = temp[-2]
    for num in arr:
        if num == first:
            print(num - second, end=" ")
        else:
            print(num - first, end=" ")
    print()
