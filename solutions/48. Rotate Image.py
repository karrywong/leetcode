class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ### Soln 0 - Jake & Karry, mathematical transformation
        for i in range(len(matrix)//2):
            matrix[i], matrix[~i] = matrix[~i], matrix[i]
            
        matrix[:] = list(map(list,zip(*matrix)))
        # matrix[:] = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
