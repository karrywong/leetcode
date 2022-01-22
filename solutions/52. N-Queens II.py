class Solution:
    def totalNQueens(self, n: int) -> int:
        #First attempt, use col, diag1, diag2 to record positions taken
        #Identical to problem 51. N-Queens
        self.count = 0
        diag1 = set([i for i in range(-n+1,n)]) # i-j, {-n+1, -n+2, ... 0, n-2, n-1}
        diag2 = set([i for i in range(0,2*n-1)]) # i+j {0, 1, 2, ..., 2*n-2}
        def backtrack(col=set(), d1 =set(), d2 = set(), A=[]):
            if len(A) == n:
                self.count += 1
                return 
                
            i = len(A) #0 <= len(A) <= n-1
            for j in range(n):
                if j not in col and i-j not in d1 and i+j not in d2:
                    A.append(j)
                    col.add(j)
                    d1.add(i-j)
                    d2.add(i+j)
                    backtrack(col, d1, d2, A)
                    A.pop() #j must be the last element
                    col.remove(j)
                    d1.remove(i-j)
                    d2.remove(i+j)
        
        backtrack()
        return self.count
                
            
        
