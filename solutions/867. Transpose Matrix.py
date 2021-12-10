class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #Time O(M*N), Space O(M*N)
        tuples = map(tuple, matrix)
        return map(list,zip(*tuples))
        
        # #Time O(N), Space(1), in-place for square matrices
        # m, n = len(matrix), len(matrix[0])
        # for i in range(m):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # return matrix        
