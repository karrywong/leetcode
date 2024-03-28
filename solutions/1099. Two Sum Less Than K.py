class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # # simpler binary search, time O(NlogN), space O(N)
        # nums.sort()
        # ans = -1
        # l, r = 0, len(nums)-1
        # while l < r:
        #     temp_val = nums[l] + nums[r]
        #     if temp_val < k:
        #         l += 1
        #         ans = max(ans, temp_val)
        #     else:
        #         r -= 1
        # return ans
        
        # # # binary search, tricky, time O(NlogN), space O(N)
        nums.sort()
        ans = -1
        for i in range(len(nums)):
            if nums[i] >= k: break
            #for every Ai, find the largest Aj with Ai+Aj<K
            l, r = i+1, len(nums)
            target = k - nums[i]
            while l < r : 
                mid = l + (r-l)//2
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid
            if l-1 > i:
                ans = max(ans,nums[i] + nums[l-1])
        return ans
