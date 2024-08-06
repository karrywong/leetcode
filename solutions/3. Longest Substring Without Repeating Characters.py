class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Recent attempt, time O(N), space O(N)
        lookup = {}
        ans = 0
        left = -1
        for right, char in enumerate(s):
            if char in lookup and lookup[char] > left:
                left = lookup[char]
            lookup[char] = right
            ans = max(ans, right-left)
        return ans
​
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
