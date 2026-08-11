n, q = map(int, input().split())
p = sorted(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + p[i]
for _ in range(q):
    x, y = map(int, input().split())
    start = n - x
    print(prefix[start + y] - prefix[start])
