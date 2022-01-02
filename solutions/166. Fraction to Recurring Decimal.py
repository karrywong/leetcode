class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        #Solution inspired by palisade in discussion
        if numerator == 0:
            return "0"
        negative = (numerator < 0 ) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        ans = ["-"] if negative else []
        q, remainder = divmod(numerator,denominator)
        ans.append(str(q))
        
        seen = {}
        if remainder == 0:
            return "".join(ans)
        ans.append(".")
        
        while remainder != 0:
            if remainder in seen:
                ans.append(")")
                start_repeat = seen[remainder]
                return "".join(ans[:start_repeat]+["("]+ans[start_repeat:])
            seen[remainder] = len(ans)
            remainder *= 10
            q, remainder = divmod(remainder,denominator)
            ans.append(str(q))
        return "".join(ans)
        
#         #Mock interview practice failed, use hashmap in recording repeating remainder
#         if numerator != denominator:
#             q, numerator = divmod(numerator,denominator)
#             if numerator == 0:
#                 return str(q)
#             else:
#                 ans = str(q)+"."
#         else:
#             return "1"
        
#         remainder = []
#         while numerator != 0 :
#             numerator *= 10
#             q, numerator = divmod(numerator,denominator)
#             if q in remainder: #repeating remainder
#                 for i in range(len(remainder)):
#                     if remainder[i] == q:
#                         ans += "(" + "".join([str(r) for r in remainder[i:]]) + ")"
#                         return ans
#                     ans += str(remainder[i])
#                 return ans
#             remainder.append(q)
#         return ans + "".join([str(r) for r in remainder])
