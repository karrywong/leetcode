class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        #Easy, first attempt
        ans = []
        i = 0
        q, r = divmod(len(s),k)
        for i in range(q):
            ans.append(s[i*k:(i+1)*k])
        return ans if r == 0 else ans + [s[q*k:]+fill*(k-r)]
