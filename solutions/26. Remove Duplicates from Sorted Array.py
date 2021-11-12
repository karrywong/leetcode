class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Recent attempt
        # n = len(nums)
        # if n == 0: return n
        # if n == 1: return n
        # pointer = 1
        # temp = nums[0]
        # for cur in range(1, n):
        #     if nums[cur] != temp:
        #         nums[pointer] = nums[cur]
        #         pointer += 1
        #         temp = nums[cur]
        # return pointer
    
        ### Soln 1 - two pointers, not optimal
        # pointer = 0
        # for i, n in enumerate(nums):
        #     if n not in nums[:pointer]:
        #         nums[pointer] = n
        #         pointer += 1
        # return pointer
        
        # ### Soln 2 - two pointer, better, still not optimal 
        # if not nums: return 0
        # temp = nums[0]
        # j = 1    
        # for i in range(1, len(nums)):
        #     if nums[i] != temp:
        #         temp = nums[i]
        #         nums[j] = temp
        #         j += 1
        # return j
        
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
