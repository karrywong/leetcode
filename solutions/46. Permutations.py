class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ### Soln 2 - recursion
        def helper(nums):
            if len(nums) == 1:
                return [nums]         
            curr = helper(nums[1:])
            return [x[:i] + [nums[0]] + x[i:] for x in curr for i in range(len(nums))]
        return helper(nums)
        
        
#         ### Soln 1 - backtracking (Heap's algorithm)
#         ###finding all solutions by exploring all potential candidates        
#         def backtrack(first = 0):
#             # if all integers are used up
#             if first == n:
#                 output.append(nums[:])
        
#             for i in range(first, n):
#                 # place i-th integer first 
#                 # in the current permutation
#                 nums[first], nums[i] = nums[i], nums[first]
#                 # use next integers to complete the permutations
#                 backtrack(first + 1)
#                 # backtrack
#                 nums[first], nums[i] = nums[i], nums[first]
        
#         n = len(nums)
#         output = []
#         backtrack()
#         return output
        
        
