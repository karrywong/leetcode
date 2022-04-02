class Solution:
    def getLucky(self, s: str, k: int) -> int:
        #Four-liner by FACEPLANT, time O(logN)
        s = "".join(str(ord(x) - ord("a") + 1) for x in s)
        for _ in range(k):
            s = str(sum(int(x) for x in s))
        return s
        
        # #First attempt, following instruction, straight forward, time O(logN)
        # digits = []
        # for char in s:
        #     val = ord(char)-ord('a')+1 
        #     if val >= 10:
        #         digits.extend(list(divmod(val, 10)))
        #     else:
        #         digits.append(val)
        # for _ in range(k):
        #     if len(digits) == 1: return digits[0]
        #     val = 0
        #     for digit in digits:
        #         val += digit
        #         digits = [int(char) for char in str(val)]
        # return sum(digits[i] * 10**(len(digits)-i-1) for i in range(len(digits)))
