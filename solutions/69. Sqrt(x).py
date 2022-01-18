class Solution:
    def mySqrt(self, x: int) -> int:
        # #Recent attempt - binary search, time O(log(x)), space O(1)
        # if x < 2: return x
        # l, r = 1, x
        # while l < r:
        #     mid = l + (r-l) // 2
        #     temp = mid*mid 
        #     if temp <= x < (mid+1)*(mid+1):
        #         return mid
        #     if temp > x:
        #         r = mid-1
        #     else:
        #         l = mid+1
        # return l
    
        ### Newton's method, fastest, time O(log(x)), space O(1)
        if x < 2:
            return x
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2        
        return int(x1)
