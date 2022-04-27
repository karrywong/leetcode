class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #soln 0 - modified binary search, time O(N), space O(1)
        n = len(nums)
        if n == 0: return [-1,-1]
        if nums[0] == nums[-1]:
            if nums[0] == target:
                return [0, n-1]
            else:
                return [-1,-1]
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                ans = [mid,mid]
                i,j = mid-1, mid+1
                while i >= 0 and nums[i] == target:
                    i -= 1
                ans[0] = i + 1
                while j <= n - 1 and nums[j] == target:
                    j += 1
                ans[1] = j - 1
                return ans
                    
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [-1,-1]
