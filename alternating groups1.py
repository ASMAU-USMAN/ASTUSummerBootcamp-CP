class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        solu = 0
        for i in range(n):
            if colors[i] != colors[(i + 1) % n] and colors[(i + 1) % n] != colors[(i + 2) % n]:
                solu += 1
        return solu
