class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ### Soln 1 - sliding window + hashmap:
        n1, n2 = len(p), len(s)
        if n1 > n2: return []
            
        lib1 = collections.Counter()
        lib2 = collections.Counter()
        res = []
        
        for i in range(n1):
            lib1[p[i]] += 1
            lib2[s[i]] += 1
​
        for i in range(n2 - n1):
            if lib1 == lib2:
                res.append(i)
            lib2[s[i+n1]] += 1
            lib2[s[i]] -= 1
            if lib2[s[i]] == 0:
                del lib2[s[i]]
                
        if lib1 == lib2:
             res.append(n2-n1)
                
        return res
    
#         ### Soln 0 - naive attempt
#         n = len(p)
#         temp = sorted(tuple(p))
#         res = []
        
#         i = 0
#         while i <= len(s) - n:
#             if sorted(tuple(s[i:i+n])) == temp:
#                 res.append(i)
#                 while i + n < len(s) and s[i] == s[i+n]:
#                     i += 1
#                     res.append(i)
#                     if i + n >= len(s): 
#                         break
#             i += 1
#         return res
        
