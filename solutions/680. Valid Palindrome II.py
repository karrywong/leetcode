class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(l:int, r:int) -> bool:
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
        if left == right:
            return True
        else:
            return check_palindrome(left+1, right) or check_palindrome(left, right-1)
        
                    
    
