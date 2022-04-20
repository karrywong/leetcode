class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # soln 1 - sliding window, unicode, Time O(len(s) + len(p)), Space O(len(p))
        ns, np = len(s), len(p)
        ans = []
        if np > ns: return []        
        
        count_p, count_s = [0]*26, [0]*26
            
        for i in range(ns):
            if i < np:
                count_p[ord(p[i])-ord('a')] += 1
                count_s[ord(s[i])-ord('a')] += 1  
            else:                      
                if count_p == count_s: 
                    ans.append(i-np)
                count_s[ord(s[i])-ord('a')] += 1
                count_s[ord(s[i-np])-ord('a')] -= 1
        
        if count_p == count_s: ans.append(ns-np)
        return ans
        
#         #soln 0 - sliding window, counters, the same as 567. Permutation in String
#         ns, np = len(s), len(p)
#         ans = []
#         if np > ns: return []
        
#         lib1 = collections.Counter(p)
#         lib2 = collections.Counter(s[:np])
        
#         for i in range(ns-np):
#             if lib1 == lib2:
#                 ans.append(i)
            
#             lib2[s[np+i]] += 1
#             lib2[s[i]] -= 1
#             if lib2[s[i]] == 0:
#                 del lib2[s[i]]
            
#         if lib1 == lib2:
#             ans.append(ns-np)
        
#         return ans
