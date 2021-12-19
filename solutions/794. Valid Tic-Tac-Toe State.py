class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        #Too many failed attempts in determing feasible configurations, lines 25-29
        hor = [[0]*3 for _ in range(2)]
        ver = [[0]*3 for _ in range(2)]
        diag = [[0,0] for _ in range(2)] #Top left to bottom right, top right to bottom left
        moves = [0, 0]
        lookup = {" ": -1, "X": 0, "O" : 1}
        
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                ind = lookup[val]
                if ind > -1:
                    hor[ind][i] += 1
                    ver[ind][j] += 1
                    if i == j:
                        diag[ind][0] += 1
                    if i + j == 2:
                        diag[ind][1] += 1
                    moves[ind] += 1
        
        # print(hor,ver,diag)
        wins = [sum([hor[i].count(3), ver[i].count(3), diag[i].count(3)]) for i in range(2)]
        # print(moves, wins)
        if (wins[0]+wins[1] == 0 and 0 <= moves[0] - moves[1] <= 1) or \
            (wins[0] >= 1 and wins[1] == 0 and moves[0] == moves[1] + 1) or \
            (wins[0] == 0 and wins[1] >= 1 and moves[0] == moves[1]):
            return True
        return False
