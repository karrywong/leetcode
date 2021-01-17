class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        lst = list(s[::-1])
        
        for i in range(len(t)):
            if t[i] == lst[-1]:
                lst.pop()
            if not lst: return True
                
        return False
