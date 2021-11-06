class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        #soln 0 - first attempt, two pointers + hashtable, optimized
        #same as 159. Longest Substring with At Most Two Distinct Characters
        seen, l = {}, 0
        ans = 0
        for r, ele in enumerate(s):
            seen[ele] = r
            if len(seen) > k:
                temp = min(seen, key = seen.get)
                l = seen[temp] + 1
                del seen[temp]
            ans = max(ans, r-l+1)
        return ans
