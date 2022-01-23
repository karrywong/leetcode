class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        #First attempt, straight-forward counting
        alice, bob = 0,0
        A_count, B_count = 0,0
        for color in colors:
            if color == 'A':
                A_count += 1
                bob += B_count - 2 if B_count >= 3 else 0
                B_count = 0
            else:
                B_count += 1
                alice += A_count - 2 if A_count >= 3 else 0 
                A_count = 0
                
        alice += A_count - 2 if A_count >= 3 else 0 
        bob += B_count - 2 if B_count >= 3 else 0
        return True if alice > bob else False
