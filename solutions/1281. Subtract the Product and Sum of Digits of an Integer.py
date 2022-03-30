class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        #time O(logN), space O(logN), inspired by lee215
        A = list(map(int, str(n)))
        return reduce(operator.mul, A)-reduce(operator.add, A)
        
        # #First attempt, time O(logN), space O(1)
        # val1, val2 = 1, 0
        # while n:
        #     n, digit = divmod(n,10)
        #     val1 *= digit
        #     val2 -= digit
        # return val1 + val2
