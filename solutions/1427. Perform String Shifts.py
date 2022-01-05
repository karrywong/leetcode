class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        #Left shift is positive, right shift negative
        #Left shift by x is equal to right shift by len(s) - x
        count = 0
        for direction, val in shift:
            count += -val if direction else val
        # right = count < 0
        # if right: 
        #     count *= -1
        count %= len(s) #modulus in Python: x%n is equivalent x-(x//n)*n
        # if right:
        #     count *= -1
        return s[count:]+s[:count]
                
