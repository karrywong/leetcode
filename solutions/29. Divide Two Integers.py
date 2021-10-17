class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #bit manipulation, O(log(dd/d)^2)
        if dividend == -2**31 and divisor == -1: return 2**31-1
        ans = 0 
        dd, d = abs(dividend), abs(divisor)
        while dd >= d:
            shift = int(log(dd,2) - log(d,2))
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
        
    #Hint 1: Bit
    # 5 = 101, 2 = 10, ans = 10
    # 6 = 110, 2 = 10, ans = 11
    # -7 = -111, 3 = 11, ans = -10
    #10 = 1010, 2 = 10, ans = 101
    #32 = 100000, 2 = 10, ans = 10000
    
    #Hint 2: 
    #soln: dd = 11101011, d = 111, ans = 100001
    # dd = 11101011 - 11100000 -> 1011 - 111 = 100
    
    
        
    
