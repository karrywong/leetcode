class Solution:
    def fib(self, n: int) -> int:
    #math formula using golden ratio, time O(logN), space O(1)
        val = sqrt(5)
        val1 = (0.5*(1+val))**n
        val2 = (0.5*(1-val))**n
        return int((val1-val2)/val)
​
    #Standard recursion w/ meo, time O(N), space O(N) due to recursion
    # def __init__(self):
    #     self.memo = {0:0, 1:1}
    # def fib(self, n: int) -> int:
    #     if n in self.memo:
    #         return self.memo[n]
    #     val = self.fib(n-1)+self.fib(n-2)
    #     self.memo[n] = val
    #     return val
