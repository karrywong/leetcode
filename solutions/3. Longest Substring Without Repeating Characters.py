class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ### Soln 2 - two pointers + hashtable, optimized
        # sliding window, s[l:r+1] always no repeated character
        n = len(s)
        l = 0
        seen = {} # dictionary time O(1); space O(n)
        ans = 0
        
        for r, char in enumerate(s):
            if char in seen and l <= seen[char]:
                l = seen[char] + 1
            seen[char] = r
            ans = max(ans, r - l + 1)   
        
        return ans
        
#         ### Soln 1 - two pointers + hashtable O(N)
#         lib = {}
#         res = 0
#         head = 0
#         tail = 0
​
#         while tail < len(s):
#             l = s[tail]
#             if l not in lib:
#                 lib[l] = ""
#                 tail += 1
#                 res = max(res, tail - head)
#             else:
#                 del lib[s[head]]
#                 head += 1
#         return res
            
    
#         ### Soln 0 - brute force O(N^3), LeetCode solution
#         n = len(s)
#         ans = 0
#         for i in range(n):
#             for j in range(i+1, n+1):
#                 if self.allUnique(s,i,j):
#                     ans = max(ans, j-i)
#         return ans
    
#     def allUnique(self, s, start, end) -> bool:
#         set_letter = set()
#         for i in range(start, end):
#             if s[i] in set_letter:
#                 return False
#             set_letter.add(s[i])
#         return True
