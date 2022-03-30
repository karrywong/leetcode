class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        #one-liner brute force, by david120
        return sum(bin(i).count('1') in (2,3,5,7,11,13,17,19,23,29,31) for i in range(left,right+1))
    
        # #Reuse the idea from https://leetcode.com/problems/counting-bits/
        # #But slow since always starts from 1
        # bitcount = [0 for _ in range(right+1)]
        # primes = (2,3,5,7,11,13,17,19)
        # count = 0
        # for i in range(1, right+1):
        #     bitcount[i] = bitcount[i&(i-1)] + 1
        #     if i >= left and bitcount[i] in primes:
        #         count += 1
        # return count
