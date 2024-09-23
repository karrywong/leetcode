class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time O(N), space O(N)
        lookup = {}
        left = -1
        ans = 0
        for right, char in enumerate(s):
            if char in lookup and lookup[char] > left:
                left = lookup[char]
            ans = max(ans, right-left)
            lookup[char] = right
        return ans
    
#         ### two pointers + hashtable, optimized
#         # sliding window, s[l:r+1] always no repeated character
#         # time O(N), N = len(s), space O(N)
#         l, ans = 0, 0
#         seen = {}
        
#         for r, char in enumerate(s):
#             if char in seen and l <= seen[char]:
#                 l = seen[char] + 1
#             seen[char] = r
#             ans = max(ans, r-l+1)
#         return ans
