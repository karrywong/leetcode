class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def getNeighbor(pt, m, n): 
            #input point coordinate, output neighbors 
            lst = []
            i,j = pt
            if i > 0:
                lst.append((i-1, j))
            if i < m-1:
                lst.append((i+1, j))
            if j > 0:
                lst.append((i, j-1))
            if j < n-1:
                lst.append((i, j+1))
            return lst
        
        def search(word, pos, pre, m, n):
            #print(pos,word,pre)
            if not word:
                return True
            
            pre[pos] = None
            lst_ngh = getNeighbor(pos, m, n)
            for ngh in lst_ngh:
                if ngh not in pre and board[ngh[0]][ngh[1]] == word[0]:
                    if search(word[1:], ngh, pre, m, n):
                        return True
                    else:
                        pre.pop(ngh)
                                           
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    if search(word[1:], (i,j), {}, m, n):
                        return True
