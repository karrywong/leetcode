class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ### Cheating - using the built-in function from itertools
        # all_perm = set(itertools.permutations(nums))
        # return [list(i) for i in all_perm]
        
        ### Soln 1 - recursion II from Permutations I with slight modification
        def helper(nums):
            if len(nums) == 1:
                return [nums]
            
            curr = helper(nums[1:])
            tmp = []
            for i in range(len(nums)):
                for x in curr:
                    tmp1 = x.copy()
                    tmp1.insert(i,nums[0])
                    if tmp1 not in tmp:
                        tmp.append(tmp1)
            return tmp
        
        return helper(nums)
        
#         ### Soln 0 - repeat solution for Permutations I and get unique elements
#         def helper(nums):
#             if len(nums) == 1:
#                 return [nums]         
#             curr = helper(nums[1:])
#             return [x[:i] + [nums[0]] + x[i:] for x in curr for i in range(len(nums))]
        
#         lst = helper(nums)
#         counts = collections.Counter(tuple(v) for v in lst)
#         return [x for x in counts.keys()]
