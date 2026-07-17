t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    seen = set()
    ans = 0
    for ch in s:
        if ch in seen:
            ans += 1
        else:
            ans += 2
            seen.add(ch)
    print(ans)
