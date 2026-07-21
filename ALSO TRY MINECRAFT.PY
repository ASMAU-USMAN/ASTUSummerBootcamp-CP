n, m = map(int, input().split())
a = list(map(int, input().split()))
forward = [0] * n
for i in range(1, n):
    forward[i] = forward[i - 1] + max(0, a[i - 1] - a[i])
reverse = [0] * n
for i in range(n - 2, -1, -1):
    reverse[i] = reverse[i + 1] + max(0, a[i + 1] - a[i])
for _ in range(m):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if s < t:
        print(forward[t] - forward[s])
    else:
        print(reverse[t] - reverse[s])

# problem link --> https://codeforces.com/problemset/problem/1709/B
