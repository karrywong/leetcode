class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        #First attempt, math
        ans = 0
        while maxDoubles and target > 1:
            ans += (target % 2)
            target //= 2
            ans += 1
            maxDoubles -= 1
        return ans + (target - 1)
