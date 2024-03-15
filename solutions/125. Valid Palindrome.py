class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Two pointers, time O(N), space O(1)
        i, j = 0, len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
        
            if not s[j].isalnum():
                j -= 1
                continue
                
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True
        
        #Direct reversal, time O(N), space O(N)
        temp = [l for l in s.lower() if l.isalnum()]
        # temp = "".join(temp)
        return temp[::-1] == temp
