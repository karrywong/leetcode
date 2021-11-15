class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        #Sort + two pointers, time O(NlogN), Space O(1)
        ans, diff, n = -1, float('inf'), len(nums)
        nums.sort()
        l, r = 0, n-1
        while l < r:
            temp = nums[l] + nums[r]
            if temp >= k:
                r -= 1
            else: #temp < k
                l += 1
                ans = max(ans, temp)
        return ans
