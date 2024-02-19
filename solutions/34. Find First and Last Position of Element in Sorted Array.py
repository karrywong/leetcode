# import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # # soln 2 - use built-in function
        # if len(nums) == 0:
        #     return [-1,-1]
        # left = bisect.bisect_left(nums, target)
        # left = -1 if left == len(nums) or nums[left] != target else left
        # right = bisect.bisect_right(nums, target)
        # right = -1 if right == 0 or nums[right-1] != target else right-1
        # return [left,right]
        
        #soln 1 - binary search, both upper and lower bounds
        #for repetitious numbers
        if len(nums) == 0:
            return [-1,-1]
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid+1
            else: 
                right = mid
        left = left if nums[left] == target else -1
        ans = [left]
        
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid
        right = right-1 if nums[right-1] == target else -1
        ans.append(right)
        return ans
    
        # Testing
        # nums = [5,7,7,8,8,10], target = 8
        # (0,5) -> (3,5) -> (3,4) -> (3,3) -> 3
        # (0,6) -> (4,6) -> (4,5) -> (5,5) -> 4
        
        # nums = [5,7,7,8,8,10], target = 6
        # (0,5) -> (0,2) -> (0,1) -> (1,1) -> -1
        # (0,6) -> (0,3) -> (0,1) -> (1,1) -> -1        
