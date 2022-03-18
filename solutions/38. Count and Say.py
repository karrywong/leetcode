class Solution:
    def countAndSay(self, n: int) -> str:
        @lru_cache(maxsize = None)
        def helper(i):
            if i == 1:
                return "1"
            s = helper(i-1)
            ans = ""
            i = 1
            count, char = 1, s[0]
            while i < len(s):
                if s[i-1] == s[i]:
                    count += 1
                else:
                    ans += str(count) + char
                    char = s[i]
                    count = 1
                i += 1
            ans += str(count) + char
            return ans
        return helper(n)
