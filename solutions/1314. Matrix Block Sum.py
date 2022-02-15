class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        #Brute force O(M*N*k^2)
        #idea from 1D: sum of subarray of arbitrary length: prefixSum = [x0, x0+x1, x0+x1+x2, ..]
        #prefixSum[i] = x0 + ... +x(i-1), sum(arr[i:j]) = prefixSum[j] - prefixSum[i-1]
        #Time O(MN), space O(MN)
        m, n = len(mat), len(mat[0])
        prefixSum = [[0] * n for _ in range(m)]
        #prefixSum[i][j] = prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]+mat[i][j]
        for i in range(m):
            for j in range(n):
                prefixSum[i][j] = mat[i][j]
                if i > 0:
                    prefixSum[i][j] += prefixSum[i-1][j]
                if j > 0:
                    prefixSum[i][j] += prefixSum[i][j-1]
                if i > 0 and j > 0:
                    prefixSum[i][j] -= prefixSum[i-1][j-1]
        #ans[i][j] = prefixSum[i+k][j+k] - prefixSum[i-k-1][j+k] - prefixSum[i+k][j-k-1] + prefixSum[i-k-1][j-k-1]
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i > k and j > k:
                    ans[i][j] += prefixSum[i-k-1][j-k-1]
                if i > k:
                    ans[i][j] -= prefixSum[i-k-1][min(j+k, n-1)]
                if j > k:
                    ans[i][j] -= prefixSum[min(i+k, m-1)][j-k-1]
                ans[i][j] += prefixSum[min(i+k, m-1)][min(j+k, n-1)]
        return ans
