class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        #BFS, time O(max(|x|,|y|)^2), space O(max(|x|,|y|)^2)
        seen = set([(x,y)])
        basicMoves = {0:[(2,1),(1,2)], 1:[(-1,2),(-2,1)], 2:[(-2,-1),(-1,-2)], 3:[(1,-2),(2,-1)]}
        queue = collections.deque([(x,y,0)])
        
        while queue:
            x0, y0, count = queue.popleft()
            if x0 == 0 and y0 == 0:
                return count
            if x0 > 0:
                if y0 > 0:
                    moves = basicMoves[1]+basicMoves[2]+basicMoves[3]
                else:
                    moves = basicMoves[0]+basicMoves[1]+basicMoves[2]
            else:
                if y0 > 0:
                    moves = basicMoves[0]+basicMoves[2]+basicMoves[3]
                else:
                    moves = basicMoves[0]+basicMoves[1]+basicMoves[3]
            
            for dx, dy in moves:
                x1, y1 = x0+dx, y0+dy
                if (x1,y1) not in seen:
                    queue.append((x1,y1,count+1))
                    seen.add((x1,y1))
