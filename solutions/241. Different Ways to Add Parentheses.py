class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:        
        #top-down DP + memo, inspired by ZitaoWang and fukinscud
        #time O(n * Catalan number) ~ O(4^n/sqrt(n)), space O(4^n/sqrt(n))
        def op(a, b, c):
            if c == '+':
                return a + b
            elif c == '-':
                return a - b
            else:
                return a * b
            
        memo = {}
        def helper(l,r):
            if l > r:
                return []
            elif expression[l:r+1].isdigit():
                return [int(expression[l:r+1])]
            elif (l,r) in memo:
                return memo[(l,r)]
            
            res = []
            for k in range(l, r+1):
                if not expression[k].isdigit():
                    left = helper(l, k-1)
                    right = helper(k+1,r)
                    res += [op(left_val, right_val, expression[k]) for left_val in left for right_val in right]
            memo[(l,r)] = res
            return res
        
        return helper(0, len(expression)-1)
​
#         #Recursion w memoization, similar
#         @lru_cache(maxsize=None)
#         def helper(string):
#             if len(string) == 0:
#                 return []
#             elif string.isdigit():
#                 return [int(string)]
            
#             res = []
#             for i in range(len(string)):
#                 if not string[i].isdigit():
#                     left = helper(string[:i])
#                     right = helper(string[i+1:])
#                     for left_val in left:
#                         for right_val in right:
#                             res.append(op(left_val, right_val, string[i]))
#             return res
#         return helper(expression)
