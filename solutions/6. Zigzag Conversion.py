class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s
        ans = []
        step = 2*numRows - 2
        for i in range(numRows):
            for j in range(i, n+step, step):
                if 0 < i < numRows-1 and 0<= j - 2*i < n:
                    ans.append(s[j-2*i])
                if 0 <= j < n:
                    ans.append(s[j])                    
        return "".join(ans)
    
        #Leetcode visit by row, much cleaner, time O(N), space O(N)
        n = len(s)
        if numRows == 1 or numRows >= n: return s
        ans = ""
        m = 2*numRows - 2
        for i in range(numRows):
            for j in range(0, n-i, m):
                ans += s[j+i]
                if i != 0 and i != numRows-1 and j+m-i < n:
                    ans += s[j+m-i]
        return ans
        
        # #First attempt - time O(N), space O(N)
        # n = len(s)
        # if numRows == 1 or numRows >= n: return s
        # m = 2*numRows - 2
        # q,r = divmod(n,m)
        # ans = "".join([s[i*m] for i in range(q)])
        # if r > 0: ans += s[-r]
        # j = 1
        # while j <= m//2:
        #     for i in range(q):
        #         ans += s[(i*m)+j]
        #         if j != m//2:
        #             ans += s[(i+1)*m-j]
        #         # print(j, i, ans)
        #     if j < r:
        #         ans += s[-r+j]
        #     if (q+1)*m - j < n and j != m//2:
        #         ans += s[(q+1)*m - j]
        #     j += 1
        # return ans
