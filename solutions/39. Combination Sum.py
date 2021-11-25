class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #soln 1 - Leetcode backtracking, optimized
        ans, n = [], len(candidates)
        def backtrack(num=target, start=0, A=[]):
            if num == 0:
                ans.append(A.copy())
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
