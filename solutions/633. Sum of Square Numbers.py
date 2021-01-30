class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ### Soln - native attempt, look at sqrt(c - i*i) for i = 0,1,2,...
        def bsearch(a, b, target):
            if a > b:
                return False
            mid = a + (b-a) // 2
            if mid * mid == target:
                return True
            if mid * mid > target:
                return bsearch(a, mid - 1, target)
            return bsearch(mid + 1, b, target)        
        
        n = floor(sqrt( c)) + 1
        for i in range(n):
            i2 = i*i
            if i2 > c:
                break
            else:
                ### use built-in square function, much faster
                m = sqrt(c - i2) 
                if m == floor(m): 
                    return True
                
                ### use binary search
                # m = c - i2
                # if bsearch(0, m, m):
                #     return True
        return False
        
​
        
