class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #soln 0 - first attempt, sorting is optional
        strs.sort(key = len)
        ans, n = strs[0], len(strs[0])
        for string in strs[1:]:
            n2 = len(string)
            i = 0
            while i < n and i < n2:
                if ans[i] == string[i]:
                    i += 1
                    continue
                break
            ans = ans[:i]
            n = len(ans)
        return ans
            
