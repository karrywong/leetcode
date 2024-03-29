class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Failed attempt, Leetcode backtrack, Time O(N*3^len(word)), Space O(len(word))
#         m, n = len(board), len(board[0])
#         moves = [(0,1), (1,0), (0,-1), (-1,0)]
#         def backtrack(i, j, target):
#             if len(target)==0:
#                 return True
#             if i < 0 or i == m or j < 0 or j == n or board[i][j] != target[0]:
#                 return False
#             board[i][j] = '#'
            
#             for move in moves:
#                 ret = backtrack(i + move[0], j + move[1], target[1:])
#                 if ret: 
#                     break
#             board[i][j] = target[0]
#             return ret
                                           
#         for i in range(0, m):
#             for j in range(0, n):
#                 if backtrack(i, j, word):
#                         return True
                    
        #Jake's solution
        m, n= len(board), len(board[0])
        
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
