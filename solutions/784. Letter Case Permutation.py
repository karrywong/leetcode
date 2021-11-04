class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        #smart - Leetcode two liners
        f = lambda x : (x.lower(), x.upper()) if x.isalpha() else x
        return [''.join(x) for x in itertools.product(*map(f,s))]   
    
#         #soln 0 - first attempt, backtracking
#         # alpha = [a for a in s if a.isalpha()]
#         lst = list(s)
#         n = len(s)
        
#         def backtrack(i=0, A=[]):
#             if len(A) == n:
#                 ans.append(''.join(A))
#                 return
            
#             if lst[i].isalpha():
#                 A.append(lst[i].lower())
#                 backtrack(i+1)
#                 A.pop()
#                 A.append(lst[i].upper())
#                 backtrack(i+1)
#                 A.pop()
#             else:
#                 A.append(lst[i])
#                 backtrack(i+1)
#                 A.pop()
                
#         ans = []
#         backtrack()
#         return ans
