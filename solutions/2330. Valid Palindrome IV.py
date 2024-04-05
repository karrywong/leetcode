class Solution:
    def makePalindrome(self, s: str) -> bool:
        neq_pair_cnt = 0
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                neq_pair_cnt += 1
            left += 1
            right -= 1
        return True if neq_pair_cnt <= 2 else False
