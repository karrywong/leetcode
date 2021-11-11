class Solution:
    def findMin(self, nums: List[int]) -> int:
        #soln 0 - binary search, similar from 33. Search in Rotated Sorted Array
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] < nums[r]: 
                return nums[l]
            
            mid = l + (r-l) // 2
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
        
        
