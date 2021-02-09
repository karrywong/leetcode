class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 2, ["()()", "(())"]
        # n = 3, ["(()())","()()()","((()))","(())()","()(())"]        
        ### Soln 1 - recursion 
        if n == 0: return ['']
        ans = set()
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.add('({}){}'.format(left, right))
        return list(ans)
        
        ### Soln 0 - first attempt
        lib = {1:set(["()"])}
        for i in range(2,n+1):
            temp = set()
            for j in range(1, i):
                for (k,h) in itertools.product(lib[j],lib[i-j]):
                    temp.add(k+h)   
            for x in lib[i-1]:
                temp.add("(" + x + ")")
            lib[i] = temp
        return lib[n]
