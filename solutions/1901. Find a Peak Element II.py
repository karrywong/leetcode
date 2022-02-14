class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        #failed attempts even after reading hints
        #Follow hints, soln by idontknoooo, time O(M*logN), space O(1)
        m, n = len(mat), len(mat[0])
        l, r = 0, n-1 #BS on column
        
        while l <= r:
            mid = l + (r-l)//2
            left = False
            for i in range(m):
                if i > 0 and mat[i-1][mid] > mat[i][mid]:
                    continue
                if mid > 0 and mat[i][mid-1] > mat[i][mid]:
                    left = True
                    continue
                if i < m-1 and mat[i+1][mid] > mat[i][mid]:
                    continue
                if mid < n-1 and mat[i][mid+1] > mat[i][mid]:
                    continue
                return [i, mid]
            if left:
                r = mid - 1
            else:
                l = mid + 1
        return []
