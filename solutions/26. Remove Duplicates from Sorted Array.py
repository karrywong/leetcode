class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[ptr-1]:
                continue
            nums[ptr] = nums[i]
            ptr += 1
        return ptr
    
        # # Same but with ptr-1
        # ptr = 0
        # for idx, num in enumerate(nums):
        #     if ptr == 0 or nums[ptr-1] != num:
        #         nums[ptr] = num
        #         ptr += 1
        # return ptr
​
        ### Soln 3 - two pointer,
        # if not nums: return 0
        # j = 0
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[j]:
        #         j += 1
        #         nums[j] = nums[i]
        # return j + 1
        
        ### Soln 4 - clever, reverse pop
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)
