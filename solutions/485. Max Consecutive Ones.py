class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0        
        for n in nums:
            if n:
                count += 1
            else:
                res = max(res, count)
                count = 0
        return max(res, count)
            
            
