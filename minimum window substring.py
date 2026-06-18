from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            need[c] += 1

        have = 0
        need_count = len(need)

        left = 0
        res = (float("inf"), 0, 0)

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                if right - left + 1 < res[0]:
                    res = (right - left + 1, left, right)
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]
