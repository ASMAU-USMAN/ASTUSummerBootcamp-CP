class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = k
        right = k
        minimum = nums[k]
        answer = nums[k]
        while left > 0 or right < len(nums)-1:
            if left == 0:
                right += 1
            elif right == len(nums)-1:
                left -= 1
            elif nums[left-1] >= nums[right+1]:
                left -= 1
            else:
                right += 1
            minimum = min(minimum, nums[left], nums[right])
            length = right - left + 1
            answer = max(answer, minimum * length)
        return answer
