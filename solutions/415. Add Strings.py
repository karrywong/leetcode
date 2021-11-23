class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #First attempt
        carry = 0
        i,j = len(num1)-1, len(num2)-1
        ans, fact = 0, 1
        while i > -1 and j > -1:
            temp = ord(num1[i]) - ord('0') + ord(num2[j]) - ord('0') + carry
            if temp >= 10:
                ans += (temp % 10) * fact
                carry = 1
            else:
                ans += temp * fact
                carry = 0
            fact *= 10
            i -= 1
            j -= 1
        ans += carry*fact
        
        while i > -1:
            ans += (ord(num1[i]) - ord('0')) * fact
            fact *= 10
            i -= 1
        while j > -1:
            ans += (ord(num2[j])- ord('0')) * fact
            fact *= 10
            j -= 1
        return str(ans)
                
                
        
