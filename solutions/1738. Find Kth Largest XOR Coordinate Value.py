class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        #DP + heap soln by lenchen1112, time O(M*N*logk), space O(M*N)
        #DP: xor it with its top_left, top, and left elements
        #Heap: maintain k largest elements
        hp = []
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if i: matrix[i][j] ^= matrix[i-1][j]
                if j: matrix[i][j] ^= matrix[i][j-1]
                if i and j: matrix[i][j] ^= matrix[i-1][j-1]
                heapq.heappush(hp, matrix[i][j])
                if len(hp) > k: heapq.heappop(hp)
        return hp[0]
    
        # #Straight forward DP, time O(M*N*log(M*N)), space O(M*N)
        # val = []
        # for i, row in enumerate(matrix):
        #     for j, cell in enumerate(row):
        #         if i: matrix[i][j] ^= matrix[i-1][j]
        #         if j: matrix[i][j] ^= matrix[i][j-1]
        #         if i and j: matrix[i][j] ^= matrix[i-1][j-1]
        #         val.append(matrix[i][j])
        # return sorted(val)[-k]
        
