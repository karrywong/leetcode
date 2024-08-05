class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        for idx, num in enumerate(nums):
            if ptr <= 1 or nums[ptr-2] != num:
                nums[ptr] = num
                ptr += 1
        return ptr
​
        # #Recent attempt
        # for i in range(len(nums)-1, 1, -1):
        #     if nums[i] == nums[i-1] == nums[i-2]:
        #         nums.pop(i)
        # return len(nums)
    
#         ### Soln 2 - two pointers, optimal
#         j = 1
#         count = 1
#         for i in range(1, len(nums)):
#             if nums[i-1] == nums[i]:
#                 count += 1
#             else:
#                 count = 1
#             if count <= 2:
#                 nums[j] = nums[i]
#                 j += 1
#         return j
