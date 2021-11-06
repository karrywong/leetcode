class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #soln 0 - first attempt, two pointers + hashtable, optimized
        seen, l = {}, 0
        ans = 0
        for r, ele in enumerate(s):
            seen[ele] = r
            if len(seen) > 2:
                temp = min(seen, key = seen.get)
                l = seen[temp] + 1
                del seen[temp]
            ans = max(ans, r-l+1)
        return ans
                
        
        
