class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
#         #soln 1 - OrderedDict, time O(Nk), Space O(k)
#         seen, l = collections.OrderedDict(), 0
#         ans = 0
#         for r, ele in enumerate(s):
#             if ele in seen:
#                 del seen[ele]
#             seen[ele] = r
            
#             if len(seen) > k:
#                 _, del_idx = seen.popitem(last = False)
#                 l = del_idx + 1
#             ans = max(ans, r-l+1)
#         return ans
    
        #soln 0 - first attempt, two pointers + hashtable, optimized
        #similar as 159. Longest Substring with At Most Two Distinct Characters
        #Time O(Nk), Space O(k)
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
