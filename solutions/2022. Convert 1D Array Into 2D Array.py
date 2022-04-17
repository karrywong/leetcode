class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        k = len(original) 
        if m*n != k: return []
        return [original[i*n:(i+1)*n] for i in range(m)]
