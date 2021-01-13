class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ### Soln 1 - hashtable
        lib = {}
        res = 0
        head = 0
        tail = 0
​
        while tail < len(s):
            l = s[tail]
            if l not in lib:
                lib[l] = ""
                tail += 1
                res = max(res, tail - head)
            else:
                del lib[s[head]]
                head += 1
        return res
            
