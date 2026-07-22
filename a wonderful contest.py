t= int(input())
for i in range(t): 
    n= int(input())
    a= list(map(int, input().split()))
    steps=[]
    for s in a:
        steps.append(100//s)
    steps.sort()
    reach=0
    for step in steps :
        if step>reach+1:
            print("NO")
            break
        reach+=100
    else:
        print("YES")
