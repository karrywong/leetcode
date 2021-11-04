class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        #soln 1 - Leetcode dynamic programming, time O(N^2)
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * n for _ in range(n)]
        ans = 0
        
        for r in range(n):
            count = 0
            for c in range(n): #count 1s to the left
                count = 0 if (r,c) in banned else count+1
                dp[r][c] = count
​
            count = 0
            for c in range(n-1,-1,-1): #count 1s to the right
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
​
        for c in range(n):
            count = 0
            for r in range(n): #count 1s to the top
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
                    
            count = 0
            for r in range(n-1,-1,-1): #count 1s to the bottom
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]
        return ans
            
        # #soln 0 - Leetcode brute force (time exceeded), time O(N^3)
        # banned = {tuple(mine) for mine in mines}
        # ans = 0
        # for r in range(n):
        #     for c in range(n):
        #         k = 0
        #         while k <= r <= n-k-1 and k <= c <= n-k-1 and \
        #         (r-k, c) not in banned and (r+k, c) not in banned and \
        #         (r, c-k) not in banned and (r, c+k) not in banned:
        #             k += 1
        #         ans = max(ans, k)
        # return ans
​
        
