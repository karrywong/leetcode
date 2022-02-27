class Solution:
    def getFactors(self, n: int) -> List[List[int]]:        
        #Soln 2, inspired by ZitaoWang's recursion 
        #Can also refer to Stefan Pochmann's soln
        #Time O(loglogN)
        def helper(num, divisor):
            res = []
            if num >= divisor:
                for i in range(divisor, int(sqrt(num))+1):
                    q, r = divmod(num, i)
                    if r == 0 and q >= i and q >= divisor:
                        res += [[i,q]]
                        res += [[i] + lst for lst in helper(q,i)]
            return res
        return helper(n,2)
        
#         #Soln 1 - First attempt, backtracking, TLE
#         ans = []
#         def backtrack(num = n, A = [], start=2, end=n):
#             if num == 1:
#                 ans.append(A[:])
#                 return
            
#             if num < 1:
#                 return
            
#             for i in range(start, end):
#                 if num % i == 0:
#                     A.append(i)
#                     quotient = num // i
#                     backtrack(quotient, A, A[-1], quotient+1)
#                     A.pop()
#         backtrack()
#         return ans
