class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #soln 1 - iterative
        ans = [1]
        for _ in range(rowIndex):
            ans = [1]+ [ans[i] + ans[i+1] for i in range(len(ans)-1)] + [1]
        return ans
    
#         #soln 0 - old attempt, recursion w memoization
#         library = {0: [1], 1: [1,1]}
​
#         def helper():
#             if rowIndex in library:
#                 return library[rowIndex]
#             else:
#                 answer = [1] * (rowIndex + 1)
#                 prevRow = self.getRow(rowIndex - 1)
#                 for j in range(1, len(prevRow)):
#                     answer[j] = prevRow[j-1] + prevRow[j]
#                 library[rowIndex] = answer
#                 return library[rowIndex]
#         return helper()
        
