            for iarr in hashes.values():
                if len(iarr) >= 2: 
                    sub = s[iarr[0]:iarr[0]+guess]
                    count = 0 
                    for i in range(len(s)-guess+1):
                        if s[i:i+guess] == sub:
                            count += 1 
                    if count >= 2:
                        self.ans = s[iarr[0]:iarr[0]+guess]
                        return True
            return False
            
        lo, hi = 0, len(s)
        while lo < hi:
            mi = (lo + hi) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return self.ans
        
#         #DP, time O(N^2), space O(N^2)
#         ans, maxlen = "", 0
#         dp = [[0]*len(s) for _ in range(len(s))]
#         for j in range(1,len(s)):
#             if s[j] == s[0]:
#                 dp[0][j] = 1
#                 ans = s[0]
#                 maxlen = len(ans)
                
#         for i in range(1,len(s)):
#             for j in range(i+1, len(s)):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i-1][j-1] + 1
#                 if dp[i][j] > maxlen:
#                     ans = s[j-dp[i][j]+1:j+1]
#                     maxlen = dp[i][j]
#         return ans
