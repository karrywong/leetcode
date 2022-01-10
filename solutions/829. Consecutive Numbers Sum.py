class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 1 #number itself counts towards one
        num = 1
        val = 1
        
        while val < n:
            num += 1
            val += num
            if (n - val) % num == 0:
                ans += 1
        return ans
