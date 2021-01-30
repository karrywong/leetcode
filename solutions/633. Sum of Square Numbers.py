class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ### Soln - native attempt, look at sqrt(c - i*i) for i = 0,1,2,...
        n = floor(sqrt( 2**31 - 1))
        for i in range(n):
            i2 = i*i
            if i2 > c:
                break
            else:
                m = sqrt(c - i*i)
                if m == floor(m):
                    return True
        return False
        
