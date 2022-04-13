class Solution:
    def getSum(self, a: int, b: int) -> int:
#         #Bit manipulation,  time O(1), space O(1)
#         x, y = abs(a), abs(b)
#         if x < y:
#             a, b = b, a
#         sign = 1 if a > 0 else -1
        
#         if a*b >= 0:
#             while y:
#                 x, y = x^y, (x&y) << 1
#         else: #x-y
#             while y:
#                 x, y = x^y, ((~x)&y) << 1
                
#         return x*sign
    
        #Leetcode's miscellaneous w/ two's complement
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)
