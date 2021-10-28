class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # soln 0 - first attempt recursion
        lst = [[1]]
        def helper(n):
            if n > 1:
                lst.append([1]+ [lst[-1][i] + lst[-1][i+1] for i in range(len(lst[-1])-1)] + [1])
                helper(n-1)
        
        if numRows > 1:
            helper(numRows)
        return lst
    
#         # soln 00 - old solution with Jake
#         pTriangle=[]
#         if numRows in library:
#             for i in range(0,numRows):
#                 pTriangle.append(library[i+1])
#             return pTriangle
#         else:
#             temp = [1]
#             previous = self.generate(numRows-1)[-1]
#             for j in range(1,numRows-1):
#                 temp.append(previous[j-1]+previous[j])
#             temp.append(1)
#             library[numRows] = temp
#             return self.generate(numRows)
