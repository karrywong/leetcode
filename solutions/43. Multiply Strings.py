class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #Leetcode - sum products from all pairs of digits
        if num1 == "0" or num2 == "0": return "0"
        ans = [0]* (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1] #reverse num1 and num2 in place
        
        for i, d1 in enumerate(num1):
            for j, d2 in enumerate(num2):
                cur = i+j
                carry = ans[cur]
                val = int(d1) * int(d2) + carry
                ans[cur] = val%10
                ans[cur+1] += val // 10
        if ans[-1] == 0: ans.pop()
        return ''.join(str(digit) for digit in reversed(ans))
        
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
