class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(substr:str, l:int, r:int) -> bool:
            while l < r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return check_palindrome(s, left+1, right) or  check_palindrome(s, left, right-1)
        return True
        
        # #Time O(N), space O(N)
        # l, r = 0, len(s)-1 #left & right pointers
        # while l < r:
        #     if s[l] == s[r]:
        #         l += 1 
        #         r -= 1
        #     else: 
        #         return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
        # return True
    
