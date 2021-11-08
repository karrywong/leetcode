class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #soln 3 - Leetcode Gauss formula
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
        
        # #soln 2 - Leetcode bit manipulation
        # ans = len(nums)
        # for i, x in enumerate(nums):
        #     ans ^= i^x
        # return ans
        
        #soln 1 - second attempt w dict, Time O(n), Space O(n)
        # n = len(nums)
        # A = set([i for i in range(n+1)])
        # return A.difference(set(nums)).pop()
        
        # #soln 0 - first attempt w sort, Time O(nlogn), Space O(1)
        # nums.sort()
        # for i, x in enumerate(nums):
        #     if i != x:
        #         return i 
        # return len(nums)
