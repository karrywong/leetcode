class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # val = len(matrix) * (len(matrix)+1) // 2
        nums = set(range(1, len(matrix)+1))
        for row in matrix:
            if set(row) != nums:
                return False
        for col in zip(*matrix):
             if set(col) != nums:
                return False
        return True
