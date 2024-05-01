class Solution:
    def romanToInt(self, s: str) -> int:
#         lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         ans = lookup[s[-1]]
        
#         for i in range(len(s)-2, -1, -1):
#             bo1 = s[i]=="I" and s[i+1] in ("V", "X")
#             bo2 = s[i]=="X" and s[i+1] in ("L", "C")
#             bo3 = s[i]=="C" and s[i+1] in ("D", "M")
            
#             val = -1 * lookup[s[i]] if bo1 or bo2 or bo3 else lookup[s[i]]
#             ans += val
#         return ans
​
        # soln 3 - backward
        table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = table[s[-1]]
        ptr = -2
        pre = s[-1]
        while ptr > -len(s)-1:
            val = table[s[ptr]]
            if val < table[pre]:
                ans -= val
            else:
                ans += val
            pre = s[ptr]
            ptr -= 1
        return ans
    
        # soln 2 - check set and if the next value is larger
        #table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        #check = set(['I','X','C'])
        #ans = 0;
        #for i in range(0,len(s)):
        #    cur = s[i]
        #    if i < len(s) - 1 and table[s[i+1]] > table[cur]:
        #        ans -= table[cur]
        #    else:
        #        ans += table[cur]
        #return ans
