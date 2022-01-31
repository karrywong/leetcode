class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #recent attempt, time O(N), space O(1)
        # i = -1
        # ans = 0
        # for j, num in enumerate(nums):
        #     if num == 0:
        #         i = j
        #     else:
        #         ans = max(ans, j-i)
        # return ans
    
        #old attempt, time O(N), space O(1)
        res = 0
        count = 0        
        for n in nums:
            if n:
                count += 1
            else:
                res = max(res, count)
                count = 0
        return max(res, count)
