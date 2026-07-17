t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    zeros = s[:k].count('0')
    ok = zeros > 0
 
    for i in range(k, n):
        if s[i - k] == '0':
            zeros -= 1
        if s[i] == '0':
            zeros += 1
        if zeros == 0:
            ok = False
            break
    if not ok:
        print("NO")
        continue
    ans = [0] * n
    small = 1
    large = n
    for i in range(n):
        if s[i] == '1':
            ans[i] = small
            small += 1
    for i in range(n):
        if s[i] == '0':
            ans[i] = large
            large -= 1
    print("YES")
    print(*ans)
