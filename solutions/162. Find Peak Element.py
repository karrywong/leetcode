class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # soln 0 - binary search
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            elif nums[mid-1] > nums[mid]:
                r = mid - 1
            else:
                return mid
        return l
    
        # #soln - BS recursion
        # def helper(l, r):
        #     if l == r:
        #         return l
        #     mid = l + (r-l)//2
        #     if nums[mid] > nums[mid+1]:
        #         return helper(l, mid)
        #     return helper(mid+1, r)
        # return helper(0, len(nums)-1)
        
        
