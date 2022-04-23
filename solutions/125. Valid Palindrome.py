class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Two pointers, time O(N), space O(N)
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True
        
        # #Direct reversal, time O(N), space O(N)
        # temp = [l for l in s.lower() if l.isalnum()]
        # # temp = "".join(temp)
        # return temp[::-1] == temp
