class Solution:            
    #s1 = "ac", s2 = "abc", s3 = "abcac"
    #hint1: dynamic programming 
    #hint2: pass pointers i and j only + use hashtable 
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #Leetcode 1D dynamic programming, Time: O(M*N), Space: O(M) or O(N) depending on len(dp)
        if len(s3) != len(s1) + len(s2):  return False
        m, n = len(s1), len(s2)
        dp = [None] * (n+1) #Use 1D arrray to store 2D matrix of M*N
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[0] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    dp[0] = dp[0] and s1[i-1] == s3[i-1] 
                else:
                    dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] == s3[i+j-1])
        return dp[-1]
        
#         #After failed mock attempt, 2D dynamic programming approach
#         #Time: O(M*N), Space: O(M*N)
#         if len(s3) != len(s1) + len(s2):  return False
#         m, n = len(s1), len(s2)
#         htb = [[None] * n  for _ in range(m)] #hashtable to speedup
        
#         def check(i,j): #helper function
#             if i == m:
#                 return s2[j:] == s3[m+j:]
#             if j == n:
#                 return s1[i:] == s3[n+i:]
#             if i == m and j == n:
#                 return True
#             #both s1[i:] and s2[j:] non-empty below
            
#             if htb[i][j] is not None: 
#                 return htb[i][j]
            
#             if s1[i] != s3[i+j] and s2[j] != s3[i+j]:
#                 htb[i][j] = False
#                 return False
#             elif s1[i] == s3[i+j] and s2[j] != s3[i+j]:
#                 bo = check(i+1, j)
#                 htb[i][j] = bo
#                 return bo
#             elif s1[i] != s3[i+j] and s2[j] == s3[i+j]:
#                 bo = check(i, j+1)
#                 htb[i][j] = bo
#                 return bo
#             else: #s1[i] == s3[i+j] and s2[j] == s3[i+j]:
#                 bo = check(i+1, j) or check(i, j+1)
#                 htb[i][j] == bo
#                 return bo
            
#         return check(0,0)        
