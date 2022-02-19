class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
#         #First attempt brute force, time O(MN), space O(1)
#         m, n = len(grid), len(grid[0])
#         if m < 3 or n < 3:
#             return 0
#         digits = set(range(1,10))
        
#         count = 0
#         for i in range(1, m-1):
#             for j in range(1, n-1):
#                 if grid[i][j] == 5:
#                     cur_digits = set()
#                     row_sum = []
#                     for k in (-1,0,1):
#                         row = grid[i+k][j-1:j+2]
#                         cur_digits.update(row)
#                         row_sum.append(sum(row) == 15)                        
#                     if cur_digits == digits and all(row_sum) and all([sum([grid[i+h][k] for h in (-1,0,1)]) == 15 for k in range(j-1,j+2)]):
#                         count += 1
#         return count
        
        #4-liner soln by lee215
        #Observations:The even must be in the corner, and the odd must be on the edge.
        #And it must be in a order like "43816729" （clockwise or anticlockwise)
        def isMagic(i, j):
            s = "".join(str(grid[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return grid[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
        return sum(isMagic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2) if grid[i + 1][j + 1] == 5)
