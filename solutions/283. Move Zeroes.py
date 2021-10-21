class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### Soln 4 from LeetCode - Optimal
        pointer = 0
        for cur in range(0, len(nums)):
            if nums[cur] != 0:
                #swap
                nums[cur], nums[pointer] = nums[pointer], nums[cur]
                pointer += 1
                
        ### Soln 1 - me and Jake Reschke
#         count1 = 0 #original list
#         count2 = 0 #position
#         length_nums = len(nums)
        
#         while count2 < length_nums: # strictly less than
#             if nums[count1] == 0:
#                 nums.pop(count1) #.pop(index)
#                 nums.append(0)
#                 count1 -= 1
#             count1 += 1
#             count2 += 1
​
        ### Soln 2 from LeetCode - two for loops
#         i = 0
#         for n in nums:
#             if n == 0:
#                 i += 1 
                
#         lst = []
#         for n in nums:
#             if n != 0:
#                 lst.append(n)
