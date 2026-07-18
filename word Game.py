t = int(input())
for _ in range(t):
    n = int(input())
    players = []
    freq = {}
    for i in range(3):
        words= input().split()
        players.append(words)
        for w in words:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
    ans=[]    
    for words in players:
        score = 0
        for w in words:
            if freq[w] == 1:
                score += 3
            elif freq[w] == 2:
                score += 1
        ans.append(score)
    print(*ans)

#https://codeforces.com/problemset/problem/1722/C
