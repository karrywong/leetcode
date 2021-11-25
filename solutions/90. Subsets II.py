class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Refer to an almost identical problem, 78. Subsets
        #soln 3 - Leetcode bit manipulation
        nums.sort()
        n, ans = len(nums), []
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            A = [nums[j] for j in range(n) if bitmask[j] == '1']
            if A not in ans:
                ans.append(A)
        return ans
        
#         #soln 2 - backtrack, Time O(NlogN + N*2^N), Space O(N*2^N)
#         nums.sort()
#         n, ans = len(nums), []
#         def backtrack(start=0, A=[]):
#             if len(A) == k and A not in ans:
#                 ans.append(A[:])
#                 return
#             for i in range(start, n):
#                 A.append(nums[i])
#                 backtrack(i+1, A)
#                 A.pop()
        
#         for k in range(n+1):
#             backtrack()
#         return ans
    
        # #soln 1 - cascading, Time O(NlogN + N*2^N), Space O(N*2^N)
        # nums.sort()
        # ans = [[]]
        # for num in nums:
        #     ans += [cur + [num] for cur in ans if cur + [num] not in ans]
        # return ans
