import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1]); idx += 2
        a = [0] * (k + 2)
        for i in range(1, k + 1):
            a[i] = int(data[idx]); idx += 1
        levels = [0] * n
        cnt = [0] * (k + 2)
        for c in range(n):
            b = int(data[idx]); idx += 1
            levels[c] = b
            cnt[b] += 1

        ops = []
        max_passes = n * k + 10
        passes = 0
        while any(levels[c] <= k for c in range(n)) and passes <= max_passes:
            passes += 1
            progressed = False
            for i in range(k, 0, -1):
                if cnt[i] == 0:
                    continue
                has_limit = (i + 1 <= k)
                limit = a[i + 1] if has_limit else None
                for c in range(n):
                    if levels[c] == i:
                        if (not has_limit) or (cnt[i + 1] < limit):
                            levels[c] = i + 1
                            cnt[i] -= 1
                            cnt[i + 1] += 1
                            ops.append(c + 1)
                            progressed = True
            if not progressed:
                break

        if any(levels[c] <= k for c in range(n)):
            out.append("-1")
        else:
            out.append(str(len(ops)))
            out.append(' '.join(map(str, ops)))

    print('\n'.join(out))

if __name__ == "__main__":
    main()
