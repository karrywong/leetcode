class Solution:
    def numDecodings(self, s: str) -> int:
        #LeetCode recursion, time O(N), space O(N)
        @lru_cache(maxsize=None)
        def dp(index) -> int:
            if index == len(s):
                return 1
            elif s[index] == '0':
                return 0
            elif index == len(s)-1:
                return 1
            
            ans = dp(index+1)
            if int(s[index:index+2]) <= 26:
                ans += dp(index+2)
            return ans
        
        return dp(0)
            
#         #First attempt, time O(N), space O(N) due to memoization and recursion
#         n, check = len(s), set([''] + [str(i) for i in range(1,27)])
#         self.ans = 0
#         self.memo = {}
#         def helper(string):
#             if len(string) == 0:
#                 return 1
            
#             if string in self.memo:
#                 return self.memo[string]
            
#             count1, count2 = 0,0
#             if string[0] != '0':
#                 count1 += helper(string[1:])
#             if len(string) > 1 and string[0:2] in check:
#                 count2 += helper(string[2:])
#             count = count1 + count2
#             self.memo[string] = count
#             return count
        
#         return helper(s)
