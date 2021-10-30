class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        #0<= x < 10: ans = 10
        #10 <= x < 100: ans = 90 - 9 (11,22,..) = 81
        #math: 9*9 = 81
        #10^2 = 100 <= x < 1000 = 10^3: 900 - (10 (110-119) - 8 (211,311,411,..)) * 9
        #math: 9*9*8 = 81*8 = 648
        #10^3 = 100 <= x < 1000 = 10^4: 
        #math: 9*9*8*7
        
        #10^(n-1) <= x < 10^n, n-digit number:
        #math: 9*9*8*7*..*(9-n+2)
        
        #soln 1 - iterative, temp val optimized 
        ans = 1
        count = 1
        temp = 1
        while count <= n:
            if count == 1:
                temp *= 9
                ans += temp 
            if count == 2:
                temp *= 9
                ans += temp
            if count >= 3:
                temp *= (9-count+2)
                ans += temp                 
            count += 1
        return ans
        
        #soln 0 - recursion
#         self.ans = 1
#         def helper(n):
#             if n == 0:
#                 return 
#             if n == 1:
#                 self.ans += 9
#             if n == 2:
#                 self.ans += 81
​
#             if n >= 3:
#                 temp = 81
#                 count = n - 2 
#                 fact = 8 
#                 while count > 0:
#                     temp *= fact 
