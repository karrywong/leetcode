class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #First attempt, straightforward
        if len(needle) == 0:
            return 0
        i = 0
        while i+len(needle)-1 < len(haystack):
            if haystack[i:i+len(needle)] == needle:
                return i
            i += 1
        return -1
