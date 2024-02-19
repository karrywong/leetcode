class Solution:
#     # Backtracking, time n-th Catalan number O(4^n/(n*sqrt(n))), space O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(lst: List[str]=[], cnt_left_brac: int=0, cnt_right_brac: int=0) -> None:
            if len(lst) == 2*n:
                ans.append("".join(lst))
                return
            
            if cnt_right_brac < cnt_left_brac:
                lst.append(")")
                backtrack(lst, cnt_left_brac, cnt_right_brac+1)
                lst.pop()
            
            if cnt_left_brac < n: 
                lst.append("(")
                backtrack(lst, cnt_left_brac+1, cnt_right_brac)
                lst.pop()          
                
        backtrack()
        return ans
    
#Testing, n=2
# ans = [()(),]
#(2,0), lst = [(())]
​
        # ## Soln 1 - recursion 
        # if n == 0: return [""]
        # ans = []
        # for c in range(n):
        #     for left in self.generateParenthesis(c):
        #         for right in self.generateParenthesis(n-1-c):
        #             ans.append("(" + left + ")" + right)
        # return ans
        
        # ### Soln 0 - first attempt
        # lib = {1:set(["()"])}
        # for i in range(2,n+1):
        #     temp = set()
        #     for j in range(1, i):
        #         for (k,h) in itertools.product(lib[j],lib[i-j]):
        #             temp.add(k+h)   
        #     for x in lib[i-1]:
        #         temp.add("(" + x + ")")
        #     lib[i] = temp
        # return lib[n]
