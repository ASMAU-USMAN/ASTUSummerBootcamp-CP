class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        n = len(nums)
        left = 0
        ans = 0

        while left < n:
            if nums[left] % 2 != 0 or nums[left] > threshold:
                left += 1
                continue

            right = left
            while right + 1 < n:
                if (nums[right + 1] > threshold or
                    nums[right + 1] % 2 == nums[right] % 2):
                    break
                right += 1

            ans = max(ans, right - left + 1)
            left = right + 1

        return ans   
