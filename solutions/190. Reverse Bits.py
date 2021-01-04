class Solution:
    def reverseBits(self, n: int) -> int:
        # return int(bin(n)[2:].zfill(32)[::-1], 2)
        n_bin = bin(n)[2:]
        if len(n_bin) < 32:
            n_bin = (32 - len(n_bin)) * "0" + n_bin
        return int(n_bin[::-1],2)
        
