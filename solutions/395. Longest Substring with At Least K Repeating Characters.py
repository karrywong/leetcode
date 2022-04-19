class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = collections.Counter(s)
        ub_unique = 1+min(len(s) // k, len(set(s)))
        ans = 0
        for target in range(1, ub_unique):
            seen = collections.Counter() #sliding window
            l = 0
            for r, char in enumerate(s):
                seen[char] += 1
                while len(seen) > target:
                    seen[s[l]] -= 1
                    if seen[s[l]] == 0:
                        del seen[s[l]]
                    l += 1
                if all([value >=k for value in seen.values()]):
                    ans = max(ans, r-l+1)
        return ans                
        
        # #4-liner Python by Stefan Pochmann
        # for c in set(s):
        #     if s.count(c) < k:
        #         return max(self.longestSubstring(t, k) for t in s.split(c))
        # return len(s)
