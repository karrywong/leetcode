class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #soln 3 - Leetcode bit manipulation
        n, ans = len(nums), []
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            
            A = []
            for j in range(n):
                if bitmask[j] == '1':
                    A.append(nums[j])
            ans.append(A)
        return ans
        
        #soln 2 - Leetcode backtracking, fastere
#         n, ans = len(nums), []
#         def backtrack(start = 0, A = []):
#             if len(A) == k:  
#                 ans.append(A[:])
#                 return
#             for i in range(start, n):
#                 A.append(nums[i])
#                 backtrack(i + 1, A)
#                 A.pop()
                
#         for k in range(n + 1):
#             backtrack()
#         return ans
        
        #soln 1 - Leetcode cascading, much faster
        # n, ans = len(nums), [[]]
        # for num in nums:
        #     ans += [cur + [num] for cur in ans]
        # return ans
    
#         #first attempt, backtracking, Time O(N*2^N), Space O(N*2^N), much slower due to repetitions
#         n, ans = len(nums), []
#         def backtrack(start=0, A=[]):
#             if A not in ans:
#                 ans.append(A[:])
            
#             for i in range(start, n):
#                 if nums[i] not in A:
#                     A.append(nums[i])
#                     backtrack(i+1, A)
#                     A.pop()
            
#         backtrack()
#         return ans
