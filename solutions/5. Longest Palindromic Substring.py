class Solution:
    def longestPalindrome(self, s: str) -> str:
        # #Soln 2 - O(n^2), logical w expand around center
        # def expandAroundCenter(s,left,right):
        #     l, r = left, right
        #     while l>=0 and r<=len(s)-1 and s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     l += 1
        #     r -= 1
        #     return r-l+1, l, r
        # start, end, length = 0,0,1
        # for i in range(len(s)):
        #     len1, l1, r1 = expandAroundCenter(s, i, i)
        #     len2, l2, r2 = expandAroundCenter(s, i, i+1)
        #     if len1 > len2 and len1 > length:
        #         start, end, length = l1, r1, len1
        #     elif len1 <= len2 and len2 > length:
        #         start, end, length = l2, r2, len2
        # return s[start:end+1]
        
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
        
        ### Soln 3 - Old attempt
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
