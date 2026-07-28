t = int(input())
for i in range(t):
    a = int(input())
    s = list(map(int, input().split()))
    if a == 1:
        print(-1)
        continue
    ans = sorted(s)
    for i in range(a - 1):
        if ans[i] == s[i]:
            ans[i], ans[i + 1] = ans[i + 1], ans[i]
    if ans[-1] == s[-1]:
        ans[-1], ans[-2] = ans[-2], ans[-1]
    print(*ans)
