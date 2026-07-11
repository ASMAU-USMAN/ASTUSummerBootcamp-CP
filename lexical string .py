t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    a = input()
    b = input()
    a = sorted(a)
    b = sorted(b)
    c = ""
    count_a = 0
    count_b = 0
    while a and b:
        if count_a == k:
            c += b.pop(0)
            count_b += 1
            count_a = 0
        elif count_b == k:
            c += a.pop(0)
            count_a += 1
            count_b = 0
        elif a[0] < b[0]:
            c += a.pop(0)
            count_a += 1
            count_b = 0
        else:
            c += b.pop(0)
            count_b += 1
            count_a = 0
    print(c)
