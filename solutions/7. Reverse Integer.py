class Solution:
    def reverse(self, x: int) -> int:
        if x > 0: 
            ans = list(str(x))
            y = int("".join(ans[::-1]))
            return y if y <= 2**31 - 1 else 0
        elif x == 0:
            return 0
        else:
            ans = list(str(-x))
            y = int("".join(ans[::-1])) * -1
            return y if y >= -2**31 else 0
