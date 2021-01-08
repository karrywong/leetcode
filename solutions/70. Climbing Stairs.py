class Solution:
    def climbStairs(self, n: int) -> int:
        temp1 = 1
        temp2 = 2
​
        if n == 1: 
            return temp1
        elif n == 2:
            return temp2
        else:
            for i in range(0, n-2):
                answer = temp1 + temp2 
                temp1 = temp2 
                temp2 = answer
            return answer
