class Solution:
    def addDigits(self, num: int) -> int:
        #soln 2 - Leetcode math, optimized
        return 1 + (num - 1) % 9 if num else 0        
               
        # #soln 1 - Leetcode math
        # if num == 0:
        #     return 0
        # if num % 9 == 0:
        #     return 9
        # return num % 9        
        
