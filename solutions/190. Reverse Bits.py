import functools
class Solution:
    def reverseBits(self, n: int) -> int:
        #soln 3 - Leetcode without loop
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
    
#         #soln 2 - Leetcode byte swap with memoization
#         ans, power = 0, 24
#         while n:
#             ans += self.reverseByte(n & 0xff) << power
#             n >>= 8 
#             power -= 8
#         return ans
    
#     @functools.lru_cache(maxsize=256)
#     def reverseByte(self, byte):
#         return (byte * 0x0202020202 & 0x010884422010) % 1023
        
        # #soln 1 - Leetcode bit manipulation
        # ans, power = 0, 31
        # while n:
        #     ans += (n & 1) << power
        #     n >>= 1
        #     power -= 1
        # return ans
        
        # #soln 0 - naive attempt, string 
        # x = bin(n)[2:]
        # x = '0'*(32-len(x)) + x
        # return int(x[::-1],2)
