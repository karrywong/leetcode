class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ### Cheating - using the built-in function from itertools
        return [list(i) for i in itertools.permutations(nums)]
        
        ### Soln 3 - recursion II
#         def helper(nums):
#             if len(nums) == 1:
#                 return [nums]
            
#             curr = helper(nums[1:])
            
#             tmp = []
#             for i in range(len(nums)):
#                 for x in curr:
#                     tmp1 = x.copy()
#                     tmp1.insert(i,nums[0])
#                     tmp.append(tmp1)
#             return tmp
#         return helper(nums)
        
        # # ### Soln 2 - recursion
        # def helper(nums):
        #     if len(nums) == 1:
        #         return [nums]         
        #     curr = helper(nums[1:])
        #     return [x[:i] + [nums[0]] + x[i:] for x in curr for i in range(len(nums))]
        # return helper(nums)
        
        ### Soln 1 - backtrack
#         n = len(nums)
#         lst = []
#         def backtrack(start = 0):
#             if start == n:
#                 lst.append(nums[:])
#                 return
​
#             for i in range(start, n):
#                 nums[i], nums[start] = nums[start], nums[i]
#                 backtrack(start+1)
#                 nums[i], nums[start] = nums[start], nums[i]
​
#         backtrack()
#         return lst
        
