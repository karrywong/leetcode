class Solution:
    def myAtoi(self, s: str) -> int:
        # Max and Min values for the integers
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # Trimmed string
        s = s.lstrip()
        # Counter
        i = 0
        # Flag to indicate if the number is negative
        isNegative = len(s) > 1 and s[0] == '-'
        # Flag to indicate if the number is positive
        isPositive = len(s) > 1 and s[0] == '+'
        if isNegative:
            i += 1
        elif isPositive:
            i += 1
        # This will store the converted number
        number = 0
        # Loop for each numeric character in the string iff numeric characters are leading
        # characters in the string
        while i < len(s) and '0' <= s[i] <= '9':
            number = number * 10 + (ord(s[i]) - ord('0'))
            i += 1
        # Give back the sign to the number
        if isNegative:
            number = -number
        # Edge cases - integer overflow and underflow
        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX
        return number
        
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
#         if sign == "-": ans *= -1
        
#         if ans < -2**31: ans = -2**31
#         elif ans > 2**31 - 1: ans = 2**31 - 1
#         return ans
