class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #Refer to an almost identical problem, 46. Permutations
        ### Cheating - using the built-in function from itertools
        # return [list(i) for i in set(itertools.permutations(nums))]
        
        # #soln 3 - recursion
        # def helper(nums):
        #     if len(nums) == 1:
        #         return [nums]
        #     curr = helper(nums[1:])
        #     return [x[:i] + [nums[0]] + x[i:] for x in curr for i in range(len(x)+1)]
        # lst = helper(nums)
        # counter = collections.defaultdict(int)
        # for v in lst:
        #     counter[tuple(v)] += 1
        # return counter.keys()
        
        #soln 2 - backtrack, faster, instead of checking list "nums not in ans"
        ans, n, counter = [], len(nums), collections.Counter(nums)
        def backtrack(A=[], lib=counter):
            if len(A) == n:
                ans.append(A[:])
                return
            for num in lib:
                if lib[num] > 0:
                    A.append(num)
                    lib[num] -= 1
                    backtrack(A, lib)
                    A.pop()
                    lib[num] += 1
        backtrack()
        return ans
        
#         #soln 1 - backtrack
#         ans, n = [], len(nums)
#         def backtrack(start=0):
#             if start == n and nums not in ans:
#                 ans.append(nums[:])
#                 return 
            
#             for i in range(start, n):
#                 nums[i], nums[start] = nums[start], nums[i]
#                 backtrack(start+1)
#                 nums[i], nums[start] = nums[start], nums[i]
#         backtrack()
#         return ans
