class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        ans = ""
        a_ascii = ord('a') - 1
        while i >= 0:
            if s[i] == "#":
                ans += chr(int(s[i-2:i]) + a_ascii)
                i -= 3
            else:
                ans += chr(int(s[i]) + a_ascii)
                i -= 1
        return ans[::-1]
