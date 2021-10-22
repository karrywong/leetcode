class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ### Soln 2 - backtracking 
        ans = []
        def backtrack(r, l, A=[]):
            if len(A) == 2*n:
                ans.append("".join(A))
                return
            
            if l < n:
                A.append("(")
                backtrack(r, l+1, A)
                A.pop()
            
            if r < l:
                A.append(")")
                backtrack(r+1, l, A)
                A.pop()
        
        backtrack(0, 0)
        return ans
        
        ### Soln 1 - recursion 
        # if n == 0: return ['']
        # ans = set()
        # for c in range(n):
        #     for left in self.generateParenthesis(c):
        #         for right in self.generateParenthesis(n-1-c):
        #             ans.add('({}){}'.format(left, right))
        # return list(ans)
        
        # ### Soln 0 - first attempt
        # lib = {1:set(["()"])}
        # for i in range(2,n+1):
