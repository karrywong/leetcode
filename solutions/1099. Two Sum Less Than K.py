class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # simpler binary search, time O(NlogN), space O(N)
        nums.sort()
        ans = -1
        l, r = 0, len(nums)-1
        while l < r:
            temp_val = nums[l] + nums[r]
            if temp_val < k:
                l += 1
                ans = max(ans, temp_val)
            else:
                r -= 1
        return ans
        
        # # # binary search, tricky, time O(NlogN), space O(N)
        # nums.sort()
        # ans = -1
        # for i in range(len(nums)):
        #     if nums[i] >= k: break
        #     #for every Ai, find the largest Aj with Ai+Aj<K
        #     l, r, res = i+1, len(nums)-1, i+1
        #     target = k - nums[i]
        #     while l <= r : 
        #         mid = l + (r-l)//2
        #         if nums[mid] < target:
        #             res = mid
        #             l = mid+1
        #         else:
        #             r = mid-1
        #     if res < len(nums) and nums[res] < target:
        #         ans = max(ans,nums[i] + nums[res])
        # return ans
