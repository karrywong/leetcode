class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # negative marking to find duplicate and missing
        # time O(N), space O(1)
        for num in nums:
            num_abs = abs(num)
            if nums[num_abs-1] > 0:
                nums[num_abs-1] *= -1
            else:
                dup = num_abs
        for i, num in enumerate(nums):
            if num > 0:
                miss = i+1
        return [dup, miss]
        
#         # Map, time O(N), space O(N)
#         lookup = {i:0 for i in range(1,len(nums)+1)}
#         for num in nums:
#             lookup[num] +=1
        
#         for x, cnt in lookup.items():
#             if cnt == 2:
#                 dup = x
#             if cnt == 0:
#                 miss = x
#         return [dup, miss] 
