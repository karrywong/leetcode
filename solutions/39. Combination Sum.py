class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         #Soln 2 - DP
#       # Initialize storage from 0 to target
#         dp = [[[]]] + [[] for _ in range(target)]
​
#         # For each candidate, create valid lists from candidate to target
#         for c in candidates:
#             for i in range(c, target + 1):
#                 dp[i] += [l + [c] for l in dp[i - c]]       
#             print(c, dp)
#         return dp[target]
        
        #soln 1 - Leetcode backtracking, optimized
        #Time O(N**(T/M+1)), space O(T/M), where T is the target value & M = min(candidates)
        ans, n = [], len(candidates)
        def backtrack(num=target, start=0, A=[]):
            if num == 0:
                ans.append(A[:])
                return
            if num < 0:
                return
            for i in range(start, n):
                A.append(candidates[i])
                backtrack(num-candidates[i], i, A)
                A.pop()
        backtrack()
        return ans
        
        #soln 0 - first attempt, backtracking with hashtable, slow
#         ans, seen, n = [], set(), len(candidates)
#         def backtrack(num, A=[], count = [0]*n):
#             tp = tuple(count)
#             if num == 0 and tp not in seen:
#                 ans.append(A.copy())
#                 seen.add(tp)
#                 return
            
#             for i, c in enumerate(candidates):
#                 if num - c >= 0:
#                     A.append(c)
#                     count[i] += 1
#                     backtrack(num-c, A, count)
#                     A.pop()
#                     count[i] -= 1
​
#         backtrack(target)
#         return ans
