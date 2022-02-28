class Solution:
    def validPalindrome(self, s: str) -> bool:
        #Time O(N), space O(1)
        l, r = 0, len(s)-1 #left & right pointers
        while l < r:
            if s[l] == s[r]:
                l += 1 
                r -= 1
            else: 
                return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
        return True
