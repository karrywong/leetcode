from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #one-pass, time O(N), space O(1)
        ans = n = blocks[:k].count('W')
        for i in range(k, len(blocks)):
            n += (blocks[i] == 'W') - (blocks[i-k] == 'W')
            ans = min(ans, n)
        return ans
