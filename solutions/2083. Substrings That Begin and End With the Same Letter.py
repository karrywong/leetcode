class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #Straightforward, mock practice, time O(N), space O(N)
        count = collections.Counter(s)
        #"abcba" -> dict = {a: 2, b:2, ...}
        ans = 0
        for k in count:
            ans += count[k] + (count[k]*(count[k]-1))//2
        return ans
            
