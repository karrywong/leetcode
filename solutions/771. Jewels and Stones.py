class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #Straightforward
        lookup = set(jewels)
        ans = 0
        for stone in stones:
            if stone in lookup:
                ans += 1
        return ans
