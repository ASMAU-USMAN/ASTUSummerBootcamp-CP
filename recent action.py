for _ in range(int(input())):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    x = set()
    c = 0
    for i in range(m):
        post = p[i]
        t = i + 1  
        if post not in x:
            x.add(post)
            c += 1
            post= n - c
            ans[post] = t
            
            if c == n:
                break
    for t in ans:
        print(t , end=" ")
    print()  
