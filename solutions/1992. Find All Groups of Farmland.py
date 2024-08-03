class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # left -> right; top->down
        def get_bottom_right(r:int, c:int) -> List[int]:
            while r < rows and land[r][c] == 1:
                r += 1 # go down
            r -= 1
            
            while c < cols and land[r][c] == 1:
                c += 1 # go right
            c -= 1
            return [r,c]
​
        
        # Time O(m*n), space O(m*n)
        rows, cols = len(land), len(land[0])
        ans = []
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 0:
                    continue
                    
                check_row = (row == 0 or land[row-1][col] == 0)
                check_col = (col == 0 or land[row][col-1] == 0)
                if check_row and check_col:
                    ans.append([row, col, *get_bottom_right(row, col)])
​
        return ans
