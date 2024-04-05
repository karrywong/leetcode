class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # nums = set(range(1, len(matrix)+1))
        n = len(matrix)
        for row in matrix:
            if len(set(row)) != n:
                return False
        for col in zip(*matrix):
             if len(set(col)) != n:
                return False
        return True
