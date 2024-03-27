class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
#         # range cache in row sweep by xil899
#         # Time O(n^2 + nq), w/ q = len(queries), time = O(nq) if q >> n, space O(n^2)
#         mat = [[0 for _ in range(n)] for _ in range(n)]
#         for query in queries:
#             row_start, col_start, row_end, col_end = query
#             for row in range(row_start, row_end+1):
#                 mat[row][col_start] += 1
#                 if col_end + 1 < n:
#                     mat[row][col_end+1] -= 1
            
#         for row in range(n):
#             for i in range(1,n):
#                 mat[row][i] += mat[row][i-1]
#         return mat
​
        # range cache, further simplified, by xil899
        # Time O(n^2+q) = O(q) if q >> n, space O(n^2)
        mat = [[0] * n for _ in range(n)]
        for query in queries:
            row_start, col_start, row_end, col_end = query
            mat[row_start][col_start] += 1
            row_end += 1
            col_end += 1
            if col_end < n:
                mat[row_start][col_end] -=1
            if row_end < n:
                mat[row_end][col_start] -= 1
            if col_end < n and row_end < n:
                mat[row_end][col_end] += 1
        for row in range(n):
            for col in range(1,n):
                mat[row][col] += mat[row][col-1]
        for col in range(n):
            for row in range(1,n):
                mat[row][col] += mat[row-1][col]
        return mat
