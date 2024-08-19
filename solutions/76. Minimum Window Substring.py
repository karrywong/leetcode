class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Too many failed attempts, LeetCode sliding window
        #Time O(len(s) + len(t)), space O(len(s) + len(t))
        if not t or not s:
            return ""
        dict_t = collections.Counter(t)
        required = len(dict_t)
        l = 0
        formed = 0
        window_counts = collections.Counter()
        
        ans = (float('inf'), None, None)
​
        for r in range(len(s)):
            char = s[r]
            window_counts[char] += 1;
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
                
            while l <= r and formed == required:
                char = s[l]
                
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1
        return "" if ans[0] == float('inf') else ''.join(s[ans[1]:ans[2]+1])
