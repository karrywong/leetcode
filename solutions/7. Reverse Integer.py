class Solution:
    def reverse(self, x: int) -> int:
        # bo = True if x >= 0 else False
        # if bo:
        #     return int(str(x)[::-1]) if int(str(x)[::-1]) <= 2**31 - 1 else 0
        # else:
        #     return -1*int(str(x)[1:][::-1]) if -1*int(str(x)[1:][::-1]) >= -2**31 else 0
        
        # Cleaner, time O(logx), space O(1)
        sign = 1 if x >= 0 else -1
        x = abs(x)
        ans = 0
        while x:
            x, rmd  = divmod(x, 10)
            ans = 10 * ans + rmd
            if (sign == 1 and ans >= 2**31) or (sign == -1 and ans > 2**31):
                return 0
            
        return sign*ans
