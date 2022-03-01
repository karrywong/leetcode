class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def place_number(d, row, col): #Place a number d in (row, col) cell
            rows[row].add(d)
            columns[col].add(d)
            boxes[box_index(row, col)].add(d)
            board[row][col] = str(d)
​
        def remove_number(d, row, col): #Remove a number which didn't lead to a solution
            rows[row].remove(d)
            columns[col].remove(d)
            boxes[box_index(row, col)].remove(d)
            board[row][col] = '.'    
        
        def place_next_numbers(row, col): #backtrack to continue to place numbers till a solution
            # Being in the last cell implies a solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else: #if not yet    
                if col == N - 1: # if we're in the end of the row go to the next row
                    backtrack(row + 1, 0)
                else: # go to the next column
                    backtrack(row, col + 1)
        
        def backtrack(row = 0, col = 0): #Backtracking
            if board[row][col] == '.': # if the cell is empty
                for d in range(1, 10): # iterate over all numbers from 1 to 9
                    if d not in rows[row] and d not in columns[col] and d not in boxes[box_index(row,col)]:
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku solved, no need to backtrack since single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
        
        #Brute force with time ~ 9**81
        #LeetCode's backtracking, time ~ (9!)**9
        n, N = 3, 9
        box_index = lambda row, col: (row//3) * 3 + col//3
        
        #init rows, columns, and boxes
        rows = [set() for _ in range(N)]
        columns = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)
        sudoku_solved = False
        backtrack()             
