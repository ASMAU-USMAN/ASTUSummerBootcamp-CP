t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    freq = {}
    for i in a:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in sorted(freq):
        print(i, end=" ")
        freq[i] -= 1

    for i in sorted(freq):
        while freq[i] > 0:
            print(i, end=" ")
            freq[i] -= 1

    print()


#https://codeforces.com/problemset/problem/1497/A
