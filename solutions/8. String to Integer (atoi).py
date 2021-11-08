class Solution:
    def myAtoi(self, s: str) -> int:
        #soln 0 - first attempt, failure in interview       
        pt, temp, ans = 0, 0, None
        sign, signs = None, ["+", "-"]
        while pt < len(s):
            if s[pt] == " ": 
                if ans == None: #white space
                    pt += 1
                    continue 
                else:
                    break
            
            if s[pt] in signs: 
                if sign == None and ans == None:
                    sign = s[pt]
                else:
                    break
                    
            if s[pt].isnumeric():
                temp *= 10
                temp += (ord(s[pt]) - ord('0'))
            ans = temp
                
            if not (s[pt].isnumeric() or s[pt] in signs): 
                break
            pt += 1
        
        if ans == None: return 0
        if sign == "-": ans *= -1
        
        if ans < -2**31: ans = -2**31
        elif ans > 2**31 - 1: ans = 2**31 - 1
        return ans
