class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # #Cheat, built-in
        # return '{:b}'.format(int(a,2)+int(b,2))
        
        #Leetcode - bit manipulation, clever!
        #Time: O(N+M), Space: O(max(N, M))
        x, y = int(a,2), int(b,2)
        while y != 0: #while carry is not equal to zero
            ans = x^y
            carry = (x&y) << 1
            x, y = ans, carry
        return bin(x)[2:]
        
#         #First attempt, time: O(max(M,N)), space: O(max(M,N)+1)
#         N = max(len(a), len(b))
#         a, b = a.zfill(N), b.zfill(N)
#         a, b = a[::-1], b[::-1]
#         ans = [0] * (N+1) #max length of answer
        
#         i, carry = 0, 0 
#         while i < N:
#             val = int(a[i]) + int(b[i]) + carry
#             if val == 1:
#                 carry, ans[i] = 0, 1
#             else:
#                 carry, ans[i] = divmod(val,2)
#             i += 1
                
#         if carry:
#             ans[i] = 1
#         else:
#             ans.pop()
        
#         return ''.join(str(digit) for digit in reversed(ans))
