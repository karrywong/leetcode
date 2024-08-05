class Solution:
    def intToRoman(self, num: int) -> str:
        # time O(logN), space O(1)
        specials = {4:"IV",5:"V", 9:"IX", 40:"XL", 50:"L", 90:"XC",  400:"CD", 500:"D", 900:"CM"}
        table = {1: "I", 10:"X", 100:"C", 1000:"M"}
        multiplier = 1
        ans = ""
        while num:
            num, rmd = divmod(num, 10)
            if rmd in specials:
                tmp = specials[multiplier*rmd]
            elif rmd > 5:
                tmp = specials[5*multiplier] + (rmd-5) * table[multiplier]
            else:
                tmp = rmd*table[multiplier]
            ans = tmp + ans
            multiplier *= 10
        return ans
​
        # # clean, time O(1), space O(1)
        # digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
        #           (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
        #           (5, "V"), (4, "IV"), (1, "I")]
        # ans = ""
        # for value, symbol in digits:
        #     if num == 0: break
        #     count, num = divmod(num, value)
        #     ans += symbol * count
        # return ans
            
