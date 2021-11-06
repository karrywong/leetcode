class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #soln 0 - first attempt, two pointers + hashtable, optimized
        #Time O(N), Space O(1)
        seen, l = {}, 0
        ans = 0
        for r, ele in enumerate(s):
            seen[ele] = r
            if len(seen) > 2:
                idx = min(seen.values())
                l = seen[s[idx]] + 1
                del seen[s[idx]]
            ans = max(ans, r-l+1)
        return ans
                
        
        
