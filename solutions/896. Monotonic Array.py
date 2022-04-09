class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #Using set, time O(N), space O(N), inspired by lee215
        bo_set = set()
        for i, j in zip(nums, nums[1:]):
            bo_set.add((i>j) - (i<j))
        return not bo_set >= {1,-1}
            
        # #First attempt, messy code, time O(N), space O(1)
        # if len(nums) < 3: return True
        # i = 0
        # while i < len(nums)-1 and nums[i] == nums[i+1]:
        #     i += 1
        # if i == len(nums)-1: return True
        # bo = nums[i] < nums[i+1]
        # if bo:
        #     return all(False if nums[i] > nums[i+1] else True for i in range(i+1,len(nums)-1))
        # else:
        #     return all(False if nums[i] < nums[i+1] else True for i in range(i+1,len(nums)-1))
