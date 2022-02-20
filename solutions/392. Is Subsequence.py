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
        i = 0
        if not s: return True
        for e in t:
            if s[i] == e:
                i += 1
                if i == len(s): return True
        return False
        
