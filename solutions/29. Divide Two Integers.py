class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #bit manipulation, O(log(dd/d)^2)
        if dividend == -2**31 and divisor == -1: return 2**31-1
        ans = 0 
        dd, d = abs(dividend), abs(divisor)
        while dd >= d:
            shift = 0
            temp = d
            while dd >= temp:
                temp <<= 1
                shift += 1
            shift -= 1
            dd -= d << shift
            ans += 1 << shift
        return ans if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) else 0-ans           
​
        # O(dd/d)
        #if dividend == -2**31 and divisor == -1: return 2**31-1
        #ans = 0 
        #dd, d = abs(dividend), abs(divisor)
        #while dd >= d:
        #    dd -= d
        #    ans += 1        
        #return ans if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) else 0-ans        
