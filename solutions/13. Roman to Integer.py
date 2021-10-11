class Solution:
    def romanToInt(self, s: str) -> int:
        #soln 3 - backward
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
        
        # soln 1 - most primitive
        #ans = 0
        #htb = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        #n = len(s)
        #ptr = 0
        #while ptr < n:
        #    if ptr == n-1:
        #        ans += htb[s[ptr]]
