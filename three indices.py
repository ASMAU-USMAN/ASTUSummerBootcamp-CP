import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    T = int(next(it))
    out_lines = []

    for _ in range(T):
        n = int(next(it))
        p = [int(next(it)) for _ in range(n)]

        # L[j] = index of smallest element in p[0..j-1]
        L = [-1] * n
        min_idx = 0
        for i in range(1, n):
            if p[i-1] < p[min_idx]:
                min_idx = i-1
            L[i] = min_idx

        found = False
        for j in range(1, n-1):
            li = L[j]
            if li == -1:
                continue
            if p[li] < p[j]:
                # find any k > j with p[k] < p[j]
                for k in range(j+1, n):
                    if p[k] < p[j]:
                        out_lines.append("YES")
                        out_lines.append(f"{li+1} {j+1} {k+1}")
                        found = True
                        break
            if found:
                break

        if not found:
            out_lines.append("NO")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
