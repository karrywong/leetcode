class Solution:
    def myAtoi(self, s: str) -> int:
        #soln 0 - first attempt, failed interview pass    
        temp, ans = 0, None
        pt = 0 
        sign = None
        while pt < len(s):
            if s[pt] == " ": #white space
                if ans == None:
                    pt += 1
                    continue 
                else:
                    break
            
            if (s[pt] == "+" or s[pt] == "-"):
                if not sign and ans == None:
                    sign = s[pt]
                else:
                    break
                    
            if s[pt].isnumeric():
                temp *= 10
                temp += (ord(s[pt]) - ord('0'))
            ans = temp
                
            if not (s[pt].isnumeric() or s[pt] == "+" or s[pt]=="-"): 
                break
            pt += 1
        
        if ans == None: return 0
        if sign == "-": ans *= -1
        
        if ans < -2**31: ans = -2**31
        elif ans > 2**31 - 1: ans = 2**31 - 1
            
        return ans
    
    #"-1+2", ans = -1
    #"-1 2", ans = -1, my = -12
    #"--1", ans = 0
        
