class Solution:            
    #s1 = "ac", s2 = "abc", s3 = "abcac"
    #hint1: dynamic programming 
    #hint2: pass pointers i and j only + use hashtable 
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):  return False
        m, n = len(s1), len(s2)
        htb = [[None for _ in range(n)] for _ in range(m)] #hashtable to speedup
        
        def check(i,j):
            if i == m:
                return s2[j:] == s3[m+j:]
            if j == n:
                return s1[i:] == s3[n+i:]
            if i == m and j == n:
                return True
            #both s1[i:] and s2[j:] non-empty below
            
            if htb[i][j] is not None: 
                return htb[i][j]
            
            if s1[i] != s3[i+j] and s2[j] != s3[i+j]:
                htb[i][j] = False
                return False
            elif s1[i] == s3[i+j] and s2[j] != s3[i+j]:
                bo = check(i+1, j)
                htb[i][j] = bo
                return bo
            elif s1[i] != s3[i+j] and s2[j] == s3[i+j]:
                bo = check(i, j+1)
                htb[i][j] = bo
                return bo
            else: #s1[i] == s3[i+j] and s2[j] == s3[i+j]:
                bo = check(i+1, j) or check(i, j+1)
                htb[i][j] == bo
                return bo
        return check(0,0)        
