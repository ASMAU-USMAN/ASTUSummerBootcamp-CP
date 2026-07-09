import sys
def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    answers = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = [int(x) for x in data[idx:idx+n]]
        idx += n
        a.sort()  
        found = False
        i = 1
        red_sum = a[n - 1]         
        blue_sum = a[0] + a[1]      
        while i + (i + 1) <= n:
            if red_sum > blue_sum:
                found = True
                break
            i += 1
            if i + (i + 1) > n:
                break  
            red_sum += a[n - i]     
            blue_sum += a[i]       
        answers.append("YES" if found else "NO")
    print("\n".join(answers))
solve()
