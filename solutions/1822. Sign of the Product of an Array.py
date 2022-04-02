class Solution:
    def arraySign(self, nums: List[int]) -> int:
        #Time O(N), space O(1), straightforward
        count = True
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                count = not count
        return 1 if count else -1
