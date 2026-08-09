class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        chars = [c for c in set(s) if s.count(c) >= k]
        ans = ""
        def check(word):
            i = 0
            for c in s:
                if i < len(word) and c == word[i]:
                    i += 1
            return i == len(word)
        def dfs(word):
            nonlocal ans
            if len(word) > len(ans) or len(word) == len(ans) and word > ans:
                ans = word
            for c in chars:
                new = word + c

                if check(new * k):
                    dfs(new)
        dfs("")
        return ans
