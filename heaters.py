class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for house in houses:
            left, right = 0, len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
            radius = min(
                abs(heaters[left] - house) if left < len(heaters) else float('inf'),
                abs(heaters[right] - house) if right >= 0 else float('inf')
            )
            ans = max(ans, radius)
        return ans
