class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        pos = 0
        even, odd = 0,0
        while n:
            if n % 2 == 1:
                if pos % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1
            pos += 1
        return [even, odd]
    
    # Testing, n = 1 = 1
    # 1 % 2 == 1, pos = 3
    # [even, odd] = [2,1], n = 1101
        
        # # Time O(m) = O(logn), space O(1) 
        # n_bin = bin(n)[2:] # "0b10110"
        # even, odd = 0,0
        # m = len(n_bin)
        # for i in range(m):
        #     if n_bin[m-i-1] == '1':
        #         if i % 2 == 0:
        #             even += 1
        #         else:
        #             odd += 1
        # return [even, odd]
        
