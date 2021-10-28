class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #soln 0 - first attempt, Time O(N), space O(N)
        def helper(lst):
            lib = collections.Counter(lst)
            del lib["."]
            for key in lib:
                if lib[key] > 1: 
                    return True
            return False
        
        m, n = len(board), len(board[0])
        for i in range(m):
            if helper(board[i]):
                return False
  
        for j in range(n):
            temp = [board[i][j] for i in range(m)]
            if helper(temp):
                print(2,j)
                return False
        
        node = [(row,col) for row in range(0,7,3) for col in range(0,7,3)]
        for coord in node:
            temp = []
            for k in range(9):
                q, r = divmod(k,3)
                temp.append(board[q+coord[0]][r+coord[1]])
            if helper(temp):
                print(2, coord)
                return False
        return True
