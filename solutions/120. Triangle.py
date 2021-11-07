class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # soln 2 - recursion w memoization
        @lru_cache(maxsize=None)
        def min_path(row, col):
            path = triangle[row][col]
            if row < len(triangle) - 1:
                path += min(min_path(row + 1, col), min_path(row + 1, col + 1))
            return path
        return min_path(0, 0)
​
        # # soln 1 - second attempt, DP not in-place
        # prev_row = triangle[0]
        # for i in range(1,len(triangle)):
        #     cur_row = [triangle[i][0]+prev_row[0]] + [0]*(i-1) + [triangle[i][-1]+prev_row[-1]]
        #     for j in range(1,i):
        #         cur_row[j] = triangle[i][j] + min(prev_row[j-1], prev_row[j])
        #     prev_row = cur_row
        # return min(prev_row)
        
        # #soln 0 - first attempt, in-place DP, bottom-up Flip Triangle upside down
        # for i in range(len(triangle)-2, -1, -1):
        #     for j in range(0,i+1):
        #         triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        # return triangle[0][0]
