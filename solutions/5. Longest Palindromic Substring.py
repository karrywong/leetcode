class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time O(N^2), space O(1)
        def expand(l, r) -> Tuple[int, int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return l, r, r-l+1
            
        left, right, ans_len = 0, 0, 0
        for i in range(len(s)):
            odd_left, odd_right, odd_len = expand(i, i)
            even_left, even_right, even_len = expand(i, i+1)
            if odd_len > even_len and odd_len > ans_len:
                left, right = odd_left, odd_right
                ans_len = odd_len
            elif even_len > odd_len and even_len > ans_len:
                left, right = even_left, even_right
                ans_len = even_len
        return s[left: right+1]
    
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
        
        # ### Soln
        # L, max_len, res, i = len(s), 1, s[0], -1
        # while i + 1 < 2 * L - max_len:
        #     i += 1
        #     if i % 2 and s[i // 2] != s[i // 2 + i % 2]:
        #         continue
        #     cur_len, left, right = 1 + i % 2, i // 2, i // 2 + i % 2
        #     while left - 1 >= 0 and right + 1 <= L - 1 and s[left - 1] == s[right + 1]:
        #         left -= 1
        #         right += 1
        #         cur_len += 2
        #     if cur_len > max_len:
        #         max_len, res = cur_len, s[left:right + 1]
        # return res
