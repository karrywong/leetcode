class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] != 9:
                digits[idx] += 1
                break
            else:
                digits[idx] = 0
                
            if digits[0] == 0:
                digits.insert(0,1)
        return digits
    
#         temp = digits[::-1]
#         val = 0
#         for i in range(0, len(temp)):
#             val += temp[i] * 10**i
        
#         val += 1
#         answer = []
#         while val != 0:
#             answer.append(val % 10)
#             val = val // 10
        
#         answer = answer[::-1]
#         if len(answer) < len(digits):
#             answer = ['0']* (len(digits) - len(answer)) + answer
        
#         return answer
        
