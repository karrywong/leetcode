class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        #Time O(1), space O(1)
        n, cur = n >> 1, n & 1
        while n:
            if cur == n & 1:
                return False
            n, cur = n >> 1, n & 1
        return True
