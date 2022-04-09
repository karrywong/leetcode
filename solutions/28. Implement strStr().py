class Solution:
    def build_lps(self, pattern):
        m = len(pattern)
        lps_array = [0] * m
        i, j = 1, 0  # start from the 2nd character in pattern
        while i < m:
            if pattern[i] == pattern[j]:
                lps_array[i] = j + 1
                j += 1
                i += 1
            else:
                if j > 0:
                    j = lps_array[j - 1]
                else:
                    lps_array[i] = 0
                    i += 1
        return lps_array
    
    def strStr(self, haystack: str, needle: str) -> int:
        #KMP, implemented by vladn
        #Time complexity: O(n + m). Space complexity: O(m), n = len(haystack), m = len(needle)
​
        # build longest proper suffix array for pattern
        lps_array = self.build_lps(needle)
​
        n, m = len(haystack), len(needle)
        i, j = 0, 0
        while i < n:
            # current characters match, move to the next characters
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            # current characters don't match
            else:
                if j > 0:  # try start with previous longest prefix
                    j = lps_array[j - 1]
                # 1st character of pattern doesn't match character in text
                # go to the next character in text
                else:
                    i += 1
​
            # whole pattern matches text, match is found
            if j == m:
                return i - m
​
        # no match was found
        return -1
        
        # #First attempt, straightforward, time O(N*M), space O(1)
        # i = 0
        # for i in range(len(haystack)-len(needle)+1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        # return -1
