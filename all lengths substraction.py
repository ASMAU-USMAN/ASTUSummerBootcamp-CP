import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    l, r = 0, n - 1
    cur = 1
    ok = True
    while l <= r:
        if p[l] == cur:
            l += 1
        elif p[r] == cur:
            r -= 1
        else:
            ok = False
            break
        cur += 1
    print("YES" if ok else "NO")
