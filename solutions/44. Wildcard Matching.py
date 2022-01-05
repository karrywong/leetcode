class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Leetcode Two-pointer, time O(SP), space O(1)
        S, P = len(s), len(p)
        i, j = 0,0
        star_idx, s_tmp_idx = -1, -1
        
        while i < S:
            if j < P and p[j] in {s[i],'?'}:
                i += 1
                j += 1
            elif j < P and p[j] == "*":
                s_tmp_idx = i
                star_idx = j
                j += 1
            elif star_idx == -1:
                return False
            else: #backtrack
                i = s_tmp_idx + 1
                s_tmp_idx = i
                j = star_idx + 1
        return all(p[k] == "*" for k in range(j,P))
    
#         #Recursion w/ memoization, slow, time O(SP), space O(SP)
#         #S = len(s) and P = len(p)
#         def cleanup(p):
#             p_cleaned = []
#             for char in p:
#                 if not p_cleaned or char != "*" or (char == "*" and p_cleaned[-1] != "*"):
#                     p_cleaned.append(char)
#             return ''.join(p_cleaned)
        
#         def dp(i,j):
#             if (i,j) not in memo:
#                 if s[i:] == p[j:] or p[j:]=="*":
#                     ans = True
#                 elif s[i:] == "" or p[j:] == "":
#                     ans = False                
#                 elif s[i] == p[j] or p[j] == "?":
#                     ans = dp(i+1,j+1)
#                 elif p[j] == "*":
