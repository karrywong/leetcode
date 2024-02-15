class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # # Leetcode soln 1, incremental
        # i = 0
        # while i < len(bits)-1:
        #     i += bits[i]+1
        # return i == len(bits)-1
        
        # Leetcode soln 2, greedy
        if len(bits) == 1: return True
        i = len(bits)-2 #sec_last_zero
        while bits[i]:
            i -= 1
        # return sum(bits[i+1:]) % 2 == 0
        return (len(bits)-2-i) % 2 == 0 #improved
