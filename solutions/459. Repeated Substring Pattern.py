class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # time O(n* sqrt(n)), time O(n)
        n = len(s)
        if n == 1: return False
        for i in range(1, n//2+1):
            if n % i == 0 and s == s[:i] * (n // i):
                return True
        return False
        
        # #Very smart idea by rsrs3 with explanation, time O(N), space O(1)
        # #<https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination>
        # ss = (s + s)[1:-1]
        # return ss.find(s) != -1
