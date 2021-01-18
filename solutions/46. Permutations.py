class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ### Soln 3 - recursion II
        def helper(nums):
            if len(nums) == 1:
                return [nums]
            
            curr = helper(nums[1:])
            
            tmp = []
            for i in range(len(nums)):
                for x in curr:
                    tmp1 = x.copy()
                    tmp1.insert(i,nums[0])
                    tmp.append(tmp1)
            return tmp
        return helper(nums)
​
        
        # ### Soln 2 - recursion
        # def helper(nums):
        #     if len(nums) == 1:
        #         return [nums]         
        #     curr = helper(nums[1:])
        #     return [x[:i] + [nums[0]] + x[i:] for x in curr for i in range(len(nums))]
        # return helper(nums)
        
        
#         ### Soln 1 - backtracking (Heap's algorithm)
#         ###finding all solutions by exploring all potential candidates        
#         def backtrack(first = 0):
#             # if all integers are used up
#             if first == n:
