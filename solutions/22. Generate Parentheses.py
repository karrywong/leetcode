class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 2, ["()()", "(())"]
        # n = 3, ["(()())","()()()","((()))","(())()","()(())"]
        # wrong ideas - operations: x + "()", "()" + x, "(x)"
        
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
        
        
