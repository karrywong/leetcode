class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Time O(N), space O(1)
        def isPalindrome(l: int, r: int) -> bool: 
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        left, right = 0, len(s)-1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        
        return isPalindrome(left, right-1) or isPalindrome(left+1, right)
        
        # "abcddceba"
        # helper(s[left:right]) or helper(s[left+1:right+1])
        # "cddc" or "ddce"
        
        # naive attempt
        # #Time O(N), space O(N)
        # l, r = 0, len(s)-1 #left & right pointers
        # while l < r:
        #     if s[l] == s[r]:
        #         l += 1 
        #         r -= 1
        #     else: 
        #         return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
        # return True
