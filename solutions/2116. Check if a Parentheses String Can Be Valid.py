class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #Clever soln 2 by lz2657, idea - range of the possible number of "(" remained
        if len(s) % 2 != 0: return False
        lo = 0
        hi = 0
        for i in range(len(s)):
            lo += 1 if locked[i] == '1' and s[i] == '(' else -1
            hi -= 1 if locked[i] == '1' and s[i] == ')' else -1
            
            # if locked[i] == '1':
            #     if s[i] == '(':
            #         lo += 1
            #         hi += 1
            #     else:
            #         lo -= 1
            #         hi -= 1
            # else:
            #     lo -= 1
            #     hi += 1
            
            lo = max(lo, 0)
            if hi < lo: 
                return False
        return lo == 0
        
#         #Clever soln 1 by linfq in discussion, two-pass, time O(N), space O(1)
#         if len(s) % 2 != 0: return False
        
#         # forward traversal, treat all unlocked Parentheses as'(' and check if there is ')'
#         # that cannot be eliminated by previous '(', if it exists, then the input s can't be valid.
#         balance = 0
#         for i in range(len(s)):
#             balance += 1 if s[i] == '(' or locked[i] == '0' else -1
#             if balance < 0:
#                 return False
        
#         #backward traversal, same logics
#         balance = 0
#         for i in range(len(s)-1,-1,-1):
#             balance += 1 if s[i] == ')' or locked[i] == '0' else -1
#             if balance < 0:
#                 return False
#         return True
