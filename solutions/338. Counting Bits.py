class Solution:
    def countBits(self, n: int) -> List[int]:
        #Two optimal variations from Leetcode, time O(N), space O(1)
        # #P(x) = P(x//2) + (x mod 2)
        # ans = [0 for _ in range(n+1)]
        # for i in range(1, n+1):
        #     ans[i] = ans[i>>1] + (i&1)
        # return ans
        
        #P(x) = P(x deleted rightmost 1 bit) + 1
        ans = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            ans[i] = ans[i&(i-1)] + 1
        return ans
        
        # #Time O(NlogN), space O(N)
        # ans = [0 for _ in range(n+1)]
        # for i in range(n+1):
        #     count = 0 
        #     m = i
        #     while m:
        #         m &= m-1
        #         count += 1
        #     ans[i] = count
        # return ans
