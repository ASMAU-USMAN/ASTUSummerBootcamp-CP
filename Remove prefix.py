t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    seen = set()
    ans = 0
    for i in range(n - 1, -1, -1):
        if arr[i] in seen:
            ans = i + 1
            break
        seen.add(arr[i])
    print(ans)
