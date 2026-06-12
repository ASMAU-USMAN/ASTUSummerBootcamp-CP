class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for  i in nums:
            count+= str(i).count(str(digit))
        return count
