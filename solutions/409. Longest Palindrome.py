class Solution:
    def longestPalindrome(self, s: str) -> int:
        #soln 0 - first attempt
        # lib = collections.Counter(s)
        # ans = 0
        # for v in lib.values():
        #     if v%2 == 0:
        #         ans += v
        #     else:
        #         ans += (v-1)
        # return ans+1 if sum(map(lambda x:x%2, lib.values())) >= 1 else ans
    
        #soln 1 - Leetcode greedy, no need to store counter
        ans = 0
        for v in collections.Counter(s).values():
            ans += v//2 * 2
            if ans % 2 == 0 and v%2 == 1:
                ans += 1
        return ans
        
