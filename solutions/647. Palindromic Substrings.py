class Solution:
    def countSubstrings(self, s: str) -> int:
        #Refer to an almost identical problem, 5. Longest Palindromic Substring
        #Soln 2 - O(n^2), logical w expand around center
        def expandAroundCenter(s, l, r):
            count = 1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            l += 1
            r -= 1
            count -= 1
            return count
        
        ans = 0
        for i in range(len(s)):
            count1, count2 = expandAroundCenter(s,i,i), expandAroundCenter(s,i,i+1)
            if count1: ans += count1
            if count2: ans += count2
        return ans
        
        #Soln 1 - O(n^2), dynamic programming
        n, ans = len(s), 0
        dp = [[None] *n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            ans += 1
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans += 1
        for j in range(2,n):
            for i in range(j-1):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans += 1
        return ans
