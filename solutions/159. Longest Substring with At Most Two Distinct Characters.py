from collections import OrderedDict
​
​
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Time O(N), Space O(N), OrderedDict + two pointers
        seen = OrderedDict()
        left = 0
        ans = 0
        for right, char in enumerate(s):
            if char in seen:
                del seen[char]
            seen[char] = right
            if len(seen) > 2:
                to_delete, idx = seen.popitem(last=False)
                left = idx+1
            ans = max(ans, right-left+1)
        return ans
        
        # #Time O(N), Space O(N), hashmap + two pointers
        # seen = {}
        # left = 0
        # ans = 0
        # for right, char in enumerate(s):
        #     seen[char] = right
        #     if len(seen) > 2:
        #         idx = min(seen.values())
        #         left = seen[s[idx]]+1
        #         del seen[s[idx]]
        #     ans = max(ans, right-left+1)
        # return ans
