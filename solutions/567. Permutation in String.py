class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ### Soln 1 - Sliding window + Hashmap
        n1, n2 = len(s1), len(s2)
        if n1 > n2 : return False
        
        lib1 = collections.Counter()
        lib2 = collections.Counter()
        for i in range(n1):
            lib1[s1[i]] += 1
            lib2[s2[i]] += 1
        
        for i in range(n2 - n1):
            if lib1 == lib2:
                return True
            lib2[s2[i + n1]] += 1
            lib2[s2[i]] -= 1
            if lib2[s2[i]] == 0:
                del lib2[s2[i]]
​
        return lib1 == lib2
        
        
#         ### Soln 0 - naive attempt
#         if len(s1) > len(s2): return False
#         if len(s1) == len(s2): 
#             x1 = sorted(tuple(s1))
#             x2 = sorted(tuple(s2))
#             if x1 == x2: 
#                 return True
#             else:
#                 return False
