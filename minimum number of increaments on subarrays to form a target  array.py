class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        min=target[0]
        for i in  range (1, len(target)):
            if target[i] > target[i-1]:
                min+=target[i]-target[i-1]
        return min
        
