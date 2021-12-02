class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #First attempt, write out num2 (more digits) and compute sum([(j*10**n)*val2 for j in num1])
        #Time O(N + M*N), Space O(1)
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        m, n = len(num1), len(num2) #m <= n
        val2, order = 0, 1
        for i in range(n-1, -1, -1):
            val2 += int(num2[i]) * order
            order *= 10
​
        val1, order = 0, 1
        ans = 0
        for i in range(m-1, -1,-1):
            val1 = int(num1[i]) * order
            ans += val1 * val2
            order *= 10
        return str(ans)
            
