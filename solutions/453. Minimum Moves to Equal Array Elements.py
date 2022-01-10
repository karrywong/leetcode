class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #Key idea: (n-1) elements increased by 1 = one element decreased by 1
        min_num = min(nums)
        ans = 0
        for num in nums:
            ans += (num - min_num)
        return ans
