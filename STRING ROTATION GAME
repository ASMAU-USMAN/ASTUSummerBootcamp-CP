t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    count = 0
    for i in range(len(s)):
        r = s[i:] + s[:i]
        ans = 1
        for j in range(len(s)-1):
            if r[j] != r[j+1]:
                ans +=1
        count =max(count, ans)
    print(count)      
