from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #one-pass, time O(N), space O(1)
        n = blocks[:k].count('W')
        ans = n
        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W': n -=1
            if blocks[i] == 'W': n += 1
            ans = min(ans, n)
        return ans
