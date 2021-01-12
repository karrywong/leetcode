class Solution:
    def longestPalindrome(self, s: str) -> str:
        ### Soln 1 - from discussion by ZitaoWang, O(n^2)
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
        # for j in range(n):
        #     for i in range(0, j-1):
        #         if s[i] == s[j] and DP[i+1][j-1]:
        #             DP[i][j] = True
        #             if max_len < j - i + 1:
        #                 ans = s[i:j+1]
        #                 max_len = j - i + 1
        # return ans
        
        
        ### Soln 2 - O(n)
        # def expandAroundCenter(s, left, right):
        #     L = left
        #     R = right
        #     while (L >= 0) and (R <= len(s)-1) and (s[L] == s[R]):
        #         L -= 1
        #         R += 1
        #     L += 1
        #     R -= 1
        #     return R - L + 1, L, R
        # start, end = 0, 0
        # for i in range(len(s)):
        #     len1, L1, R1 = expandAroundCenter(s, i, i)
        #     len2, L2, R2 = expandAroundCenter(s, i, i+1)
        #     if len1 > len2 and len1 > end - start:
        #         start, end = L1, R1
        #     elif len1 <= len2 and len2 > end - start:
        #         start, end = L2, R2
        # return s[start:end+1]
        
        ### Soln 3 - O(n)
        L, max_len, res, i = len(s), 1, s[0], -1
        while i + 1 < 2 * L - max_len:
            i += 1
            if i % 2 and s[i // 2] != s[i // 2 + i % 2]:
                continue
            cur_len, left, right = 1 + i % 2, i // 2, i // 2 + i % 2
            while left - 1 >= 0 and right + 1 <= L - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
                cur_len += 2
            if cur_len > max_len:
                max_len, res = cur_len, s[left:right + 1]
        return res
