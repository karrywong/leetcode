# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
​
class Solution:
    def guessNumber(self, n: int) -> int:
        #Stefan Pochmann, cleaner
        lo, hi = 1, n
        while lo < hi:
            mid = lo + ((hi-lo)>>1)
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
        # #First attempt
        # l, r = 1, n
        # while l < r:
        #     choice = l + ((r-l)>>1)
        #     val = guess(choice)
        #     if val == 0:
        #         return choice
        #     elif val == 1:
        #         l = choice+1
        #     else:
        #         r = choice-1        
        # return l
