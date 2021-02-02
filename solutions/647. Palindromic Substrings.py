class Solution:
    def countSubstrings(self, s: str) -> int:
        ## Soln 0 - O(n), idea from Q5 Longest Palindromic Substring
        def expandAroundCenter(s, left, right):
            count = 0
            L = left
            R = right
            while (L >= 0) and (R <= len(s)-1) and (s[L] == s[R]):
                count += 1
                L -= 1
                R += 1
            return count
        
        res = 0
        for i in range(len(s)):
            res += expandAroundCenter(s, i, i)
            res += expandAroundCenter(s, i, i+1)
        return res
