t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    answer = []
    level = a[0]

    for i in range(n):
        total += a[i]
        average = total // (i + 1)
        level = min(level, average)
        answer.append(level)
    print(*answer)
