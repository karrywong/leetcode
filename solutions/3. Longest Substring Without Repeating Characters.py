class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         # time O(N), space O(N)
#         # dict = {a:0, b:1}
#         # ans = max(ans, i-dict['b'])
        
#         # s="pwwkew"
#         # (0,1,-1), (1,2,-1), (2,2,1),..., (4,3,1)
        
#         lookup = defaultdict(lambda:-1)
#         ans = 0
#         j = -1 # left bound
#         for i, c in enumerate(s):
#             if c in lookup:
#                 j = max(j,lookup[c])
#             ans = max(ans, i-j)
#             lookup[c] = i
#             # print(i,ans,j)
#         return ans
#     # (0,1,-1), (1,2,-1), (2,2,1), (3,2,)
    
​
        ### Soln 2 - two pointers + hashtable, optimized
        # sliding window, s[l:r+1] always no repeated character
        # time O(N), N = len(s), space O(N)
        n, l = len(s), 0
        seen = {}
        ans = 0
        
        for r, char in enumerate(s):
            if char in seen and l <= seen[char]:
                l = seen[char] + 1
            seen[char] = r
            ans = max(ans, r-l+1)
        return ans
