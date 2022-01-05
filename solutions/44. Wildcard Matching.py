class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Recursion w/ memoization, slow, time O(SP), space O(SP)
        #S = len(s) and P = len(p)
        def cleanup(p):
            p_cleaned = []
            for char in p:
                if not p_cleaned or char != "*" or (char == "*" and p_cleaned[-1] != "*"):
                    p_cleaned.append(char)
            return ''.join(p_cleaned)
        
        def dp(i,j):
            if (i,j) not in memo:
                if s[i:] == p[j:] or p[j:]=="*":
                    ans = True
                elif s[i:] == "" or p[j:] == "":
                    ans = False                
                elif s[i] == p[j] or p[j] == "?":
                    ans = dp(i+1,j+1)
                elif p[j] == "*":
                    ans = dp(i,j+1) or dp(i+1,j)
                else:
                    ans = False
                memo[(i,j)] = ans
            return memo[(i,j)]
        
        memo = {}
        p = cleanup(p)
        if p == s or p == "*":
            return True
        return dp(0,0)
                    
