class Solution:
    def isUgly(self, n: int) -> bool:
        #Recursion
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            mod2 = n%2
            mod3 = n%3
            mod5 = n%5
            if mod2 != 0 and mod3 != 0 and mod5 != 0:
                return False
            elif mod2 == 0:
                return self.isUgly(n//2)
            elif mod3 == 0:
                return self.isUgly(n//3)
            else:
                return self.isUgly(n//5)
