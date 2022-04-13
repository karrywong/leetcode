class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #Schoolbook's solution, time O(max(N1, N2)), space O(max(N1, N2)) w/ N1 = len(num1), N2 = len(num2)
        ans = []
        carry = 0
        p1 = len(num1)-1
        p2 = len(num2)-1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            carry, value = divmod(x1+x2+carry, 10)
            ans.append(value)
            p1 -= 1
            p2 -= 1
        
        if carry:
            ans.append(carry)
        
        return ''.join(str(x) for x in ans[::-1])
        
#         #First attempt
#         carry = 0
#         i,j = len(num1)-1, len(num2)-1
#         ans, fact = 0, 1
#         while i > -1 and j > -1:
#             temp = ord(num1[i]) - ord('0') + ord(num2[j]) - ord('0') + carry
#             if temp >= 10:
#                 ans += (temp % 10) * fact
#                 carry = 1
#             else:
#                 ans += temp * fact
#                 carry = 0
#             fact *= 10
#             i -= 1
#             j -= 1
#         ans += carry*fact
        
#         while i > -1:
#             ans += (ord(num1[i]) - ord('0')) * fact
#             fact *= 10
#             i -= 1
#         while j > -1:
#             ans += (ord(num2[j])- ord('0')) * fact
#             fact *= 10
#             j -= 1
#         return str(ans)
