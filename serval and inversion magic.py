import sys
def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    answers = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        s = data[idx].decode(); idx += 1
        half = n // 2
        bad = []
        for i in range(half):
            if s[i] != s[n - 1 - i]:
                bad.append(i)
        if not bad:
            answers.append("Yes")
        else:
            # check if bad indices are contiguous: no gaps between min and max
            if bad[-1] - bad[0] + 1 == len(bad):
                answers.append("Yes")
            else:
                answers.append("No")
    print("\n".join(answers))
solve()
