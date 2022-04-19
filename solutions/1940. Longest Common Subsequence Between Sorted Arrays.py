class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        ans = arrays[0]
        
        for k in range(1, len(arrays)):
            if len(ans) == 0:
                return []
            m, n = len(ans), len(arrays[k])
            i, j = 0, 0
            temp = []
            while i < m and j < n:
                if ans[i] < arrays[k][j]:
                    i += 1
                elif ans[i] > arrays[k][j]:
                    j += 1
                else:
                    temp.append(ans[i])
                    i += 1
                    j += 1
            ans = temp
        return ans
