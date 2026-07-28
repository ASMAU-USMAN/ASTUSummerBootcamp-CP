for i  in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    from collections import Counter
    freq=Counter(arr)
    if  any(i>=2 for i in freq.values()):
        print("YES")
    else:
        print("NO")
  
