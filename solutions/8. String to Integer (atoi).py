class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        ans = 0
        ptr = 0
        multipler = 1
        
        if len(s) == 0 or s[0] not in ("+", "-") and not s[0].isdigit():
            return ans
        elif s[0] in ("+", "-"):
            multipler = -1 if s[0]=="-" else 1
            ptr += 1
​
        upper_bound = 2**31-1
        lower_bound = 2**31
        while ptr < len(s) and s[ptr].isdigit():
            ans = ans*10 + int(s[ptr])
            if multipler == 1 and ans > upper_bound: return upper_bound
            if multipler == -1 and ans > lower_bound: return -1*lower_bound
            ptr += 1
        return ans*multipler
​
#         # improved, time O(N), space O(1)
#         upper_bound = 2**31-1
#         lower_bound = 2**31       
        
#         s = s.lstrip() # trimmed string
#         is_pos = len(s) > 1 and s[0] == "+"
#         is_neg = len(s) > 1 and s[0] == "-"
#         idx = 1 if is_pos or is_neg else 0
        
#         ans = 0
#         while idx < len(s) and s[idx].isdigit():
#             ans = ans*10 + int(s[idx])
#             if not is_neg and ans > upper_bound:
#                 return upper_bound
#             if is_neg and ans > lower_bound:
#                 return -lower_bound
#             idx += 1
​
#         return -ans if is_neg else ans
