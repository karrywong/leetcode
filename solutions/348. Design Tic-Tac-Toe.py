class TicTacToe:
    def __init__(self, n: int):
        #Mock interview, points deducted in coding style
        
        #n horizontal (0 to n-1), 
        #n vertical (n to 2n-1)
        #2 diagonals (top left -> bottom right -2, top right -> bottom left -1)
        self.arr = [[0] * (2*n+2) for _ in range(2)] #dim 2*(2n+2)
        self.n = n
​
    def move(self, row: int, col: int, player: int) -> int:
        i = player - 1
        self.arr[i][row] += 1
        if self.arr[i][row] == self.n: return player
​
        self.arr[i][self.n+col] += 1
        if self.arr[i][self.n+col] == self.n: return player
​
        if row == col:
            self.arr[i][-2] += 1
            if self.arr[i][-2] == self.n: return player
        if row + col == self.n-1:
            self.arr[i][-1] += 1            
            if self.arr[i][-1] == self.n: return player
​
        return 0 
#arr = [1,0,3,2,1,1,1,1], [1,2,0,1,1,1,1,1]
​
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
