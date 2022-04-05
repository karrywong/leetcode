class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ### Old attempt - use i and ~i and iterate through entire matrix
        return sum([mat[i][i] + mat[i][~i] if i - ~i != len(mat) else mat[i][i] for i in range(len(mat))])     
