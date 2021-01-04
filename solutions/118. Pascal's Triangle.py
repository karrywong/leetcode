class Solution:
    def generate(self, numRows: int, library = {0:[],1:[1],2:[1,1]}) -> List[List[int]]:
        pTriangle=[]
        if numRows in library:
            for i in range(0,numRows):
                pTriangle.append(library[i+1])
            return pTriangle
        else:
            temp = [1]
            previous = self.generate(numRows-1)[-1]
            for j in range(1,numRows-1):
                temp.append(previous[j-1]+previous[j])
            temp.append(1)
            library[numRows] = temp
​
            return self.generate(numRows)
        
