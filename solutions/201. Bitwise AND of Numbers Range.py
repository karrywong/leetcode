class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #soln 2 - Brian Kernighan's algorithm
        #Refer to <http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan>
        m, n = left, right
        while (m < n):
            n &= n-1
        return m & n 
        
        # #soln 1 - bit shift
        # m, n, count = left, right, 0
        # while m != 0 and n != 0 and m != n:
        #     m >>= 1
        #     n >>= 1
        #     count += 1
        # if m == 0 or n == 0: 
        #     return 0
        # else:
        #     return m << count
        
        # #Brute-force, time O(right-left+1), TLE
        # ans = left
        # for i in range(left+1, right+1):
        #     ans &= i
        # return ans
