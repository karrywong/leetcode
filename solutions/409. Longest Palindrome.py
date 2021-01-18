class Solution:
    def longestPalindrome(self, s: str) -> int:
        ### Soln 1 -  optimized
        counts = collections.Counter(s)
        res = 0
        for x in counts.values():
            res += x // 2 * 2
            if res % 2 == 0 and x % 2 == 1:
                res += 1
        return res
​
        ### Soln 2 - two liners by agave
        # c = collections.Counter(s)
        # return sum(v - 1 * (v % 2 != 0) for v in c.values()) + 1 * any(v % 2 != 0 for v in c.values())
