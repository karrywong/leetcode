class Solution:
    def myAtoi(self, s: str) -> int:
        # improved, time O(N), space O(1)
        upper_bound = 2**31-1
        lower_bound = 2**31       
        
        s = s.lstrip() # trimmed string
        is_pos = len(s) > 1 and s[0] == "+"
        is_neg = len(s) > 1 and s[0] == "-"
        idx = 1 if is_pos or is_neg else 0
        
        ans = 0
        while idx < len(s) and s[idx].isdigit():
            ans = ans*10 + int(s[idx])
            if not is_neg and ans > upper_bound:
                return upper_bound
            if is_neg and ans > lower_bound:
                return -lower_bound
            idx += 1
​
        return -ans if is_neg else ans
            
#         #soln 0 - first attempt, failure in interview       
#         pt, temp, ans = 0, 0, None
#         sign, signs = None, ["+", "-"]
#         while pt < len(s):
#             if s[pt] == " ": 
#                 if ans == None: #white space
#                     pt += 1
#                     continue 
#                 else:
#                     break
            
#             if s[pt] in signs: 
#                 if sign == None and ans == None:
#                     sign = s[pt]
#                 else:
#                     break
                    
#             if s[pt].isnumeric():
#                 temp *= 10
#                 temp += (ord(s[pt]) - ord('0'))
#             ans = temp
                
#             if not (s[pt].isnumeric() or s[pt] in signs): 
#                 break
#             pt += 1
        
#         if ans == None: return 0
