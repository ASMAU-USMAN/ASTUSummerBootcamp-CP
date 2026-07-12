t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left = 0
    right = n - 1
    count = 0
    while left < right:
        while left < right and arr[left] == 0:
            left += 1
        while left < right and arr[right] == 1:
            right -= 1
        if left < right:
            count += 1
            left += 1
            right -= 1
    print(count)
