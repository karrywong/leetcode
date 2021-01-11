class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = len(nums) - 1
        left = 0
        res = -1
        
        while left < right:
            temp = nums[right] + nums[left]
            if temp >= k:
                right -= 1
            else:
                res = max(res, temp)
                left += 1
        
        return res
