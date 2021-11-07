class Solution:
    def hammingWeight(self, n: int) -> int:
        #soln 2 - mask
        count = 0
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                count += 1
            mask <<= 1
        return count
        
        #soln 1 - counting right most 1s
        count = 0
        while n:
            n = n&(n-1)
            count += 1
        return count
    
        #soln 0 - first attempt
        return bin(n)[2:].count('1')
        
