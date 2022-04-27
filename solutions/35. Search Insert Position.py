class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # #Binary search, time O(N), space O(1)
        # i, j = 0, len(nums)-1
        # while i <= j:
        #     mid = i + ((j-i) >> 1) #better than division
        #     if nums[mid] < target:
        #         i = mid + 1
        #     elif nums[mid] > target:
        #         j = mid - 1
        #     else:
        #         return mid
        # return i
        
        #built-in binary search
        return bisect.bisect_left(nums, target)
