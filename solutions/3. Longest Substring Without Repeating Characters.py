class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#       # Soln - not well-written
#         # dict = {a:0, b:1}
#         # ans = max(ans, i-dict['b'])
​
#         lookup = defaultdict(lambda:-1)
#         ans = 0
#         j = -1 # left bound
#         for i, c in enumerate(s):
#             if c in lookup:
#                 j = max(j,lookup[c])
#             ans = max(ans, i-j)
#             lookup[c] = i
#         return ans    
​
        ### two pointers + hashtable, optimized
        # sliding window, s[l:r+1] always no repeated character
        # time O(N), N = len(s), space O(N)
        l, ans = 0, 0
        seen = {}
        
        for r, char in enumerate(s):
            if char in seen and l <= seen[char]:
                l = seen[char] + 1
            seen[char] = r
            ans = max(ans, r-l+1)
        return ans
