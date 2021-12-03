class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Leetcode Textbook addition with carry, clean, time O(N), space O(N)
        n = len(digits)
        for idx in range(n-1, -1, -1):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        return [1] + digits
        
        # # My first attempt in-place, time O(N), space O(N)
        # val = digits[-1] + 1
        # carry, digits[-1] = divmod(val, 10)
        # if carry == 0: 
        #     return digits
        # i = -2
        # while -i <= len(digits) and carry == 1:
        #     val = digits[i]+carry
        #     carry, digits[i] = divmod(val, 10)
        #     i -= 1
        # return [1]+digits if carry else digits
