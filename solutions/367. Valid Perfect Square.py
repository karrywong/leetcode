class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ## use built-in function
        # n = sqrt(num)
        # return floor(n) == n
        
        ## use binary search
        def bsearch(a, b, target):
            if a > b:
                return False
            mid = a + (b-a) // 2
            if mid * mid == target:
                return True
            if mid * mid > target:
                return bsearch(a, mid - 1, target)
            return bsearch(mid + 1, b, target)
        
        return bsearch(0,num, num)
