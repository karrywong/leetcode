class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         #soln 2
#         if not s: return True
#         lst = list(s[::-1])
        
#         for e in t:
#             if e == lst[-1]:
#                 lst.pop()
#             if not lst: return True
#         return False
        
        #soln 1
        idx = 0
        for e in t:
            if idx == len(s):
                break
            if s[idx] == e:
                idx += 1
        return idx == len(s)
        
