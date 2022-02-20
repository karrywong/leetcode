class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        #Failed attempt, inspired by one-pass LeetCode solution
        #time O(N), space O(1)
        ns, nt = len(s), len(t)
        if ns > nt:
            s, t = t, s
            ns, nt = nt, ns
            
        if nt - ns > 1:
            return False
        
        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt: # if strings have the same length
                    return s[i+1:] == t[i+1:] 
                else: # if strings have different lengths
                    return s[i:] == t[i+1:]
        return ns+1 == nt
