class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ### Soln 0 - naive attempt
        n = len(p)
        temp = sorted(tuple(p))
        res = []
        
        i = 0
        while i <= len(s) - n:
            if sorted(tuple(s[i:i+n])) == temp:
                res.append(i)
                while i + n < len(s) and s[i] == s[i+n]:
                    i += 1
                    res.append(i)
                    if i + n >= len(s): 
                        break
            i += 1
        return res
        
