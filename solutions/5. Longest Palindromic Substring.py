class Solution:
    def longestPalindrome(self, s: str) -> str:
        # #Soln 2 - O(n^2), space O(1), idea is to expand around center
        def expand(l:int, r:int) -> Tuple[int,int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return l, r
        ans_left, ans_right, ans_length = 0, 0, 0
        for i in range(len(s)):
            left1, right1 = expand(i, i)
            left2, right2 = expand(i, i+1)
            len1, len2 = right1-left1+1, right2-left2+1
            if len1 > len2 and len1 > ans_length:
                ans_left, ans_right, ans_length = left1, right1, len1
            elif len2 >= len1 and len2 > ans_length:
                ans_left, ans_right, ans_length = left2, right2, len2
        return s[ans_left:ans_right+1]
        
        # #Soln 1 - by ZitaoWang, Dynamic Programming O(n^2)
        # ans = ''
        # max_len = 0
        # n = len(s)
        # DP = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     DP[i][i] = True
        #     max_len = 1
        #     ans = s[i]
        # for i in range(n-1):
        #     if s[i] == s[i+1]:
        #         DP[i][i+1] = True
        #         ans = s[i:i+2]
        #         max_len = 2
        # for j in range(2,n):
        #     for i in range(0, j-1):
        #         if s[i] == s[j] and DP[i+1][j-1]:
        #             DP[i][j] = True
        #             if max_len < j - i + 1:
        #                 ans = s[i:j+1]
        #                 max_len = j - i + 1
        # return ans
        
        # ### Soln 3 - Old attempt, 
        # L, max_len, res, i = len(s), 1, s[0], -1
        # while i + 1 < 2 * L - max_len:
        #     i += 1
        #     if i % 2 and s[i // 2] != s[i // 2 + i % 2]:
