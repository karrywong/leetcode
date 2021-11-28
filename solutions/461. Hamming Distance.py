class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #use built-in bit count
        return bin(x^y).count('1')
        
        # #First attempt, XOR and count ones
        # #More challenging, refer to 201. Bitwise AND of Numbers Range
        # x ^= y
        # count = 0
        # while x:
        #     x &= x-1
        #     count += 1
        # return count
        
