class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #Time O(N), Space O(1)
        seen = {}
        left = 0
        ans = 0
        for right, char in enumerate(s):
            seen[char] = right
            if len(seen) > 2:
                idx = min(seen.values())
                left = seen[s[idx]]+1
                del seen[s[idx]]
            ans = max(ans, right-left+1)
        return ans
