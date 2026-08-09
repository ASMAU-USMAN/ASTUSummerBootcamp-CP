n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
total = 0
for x in b:
    while x > total + a[i]:
        total += a[i]
        i += 1
    print(i + 1, x - total)
