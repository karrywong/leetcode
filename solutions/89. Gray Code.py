class Solution:
    def grayCode(self, n: int) -> List[int]:
        # # wikipedia https://en.wikipedia.org/wiki/Gray_code#Converting_to_and_from_Gray_code
        # return [i ^ (i >> 1) for i in range((1<<n))]
        
        # recursion, time O(2^n), space O(n)
        if n == 1:
            return [0,1]
        res = self.grayCode(n-1)
        mask = 1<<(n-1)
        return res + [r | mask for r in res][::-1]
        
#         # improved bit manipulation, time O(n*2^n), space (2^n)
#         ans = []
#         seen = set()
#         def backtrack(x: int=0) -> None:
#             ans.append(x)
#             seen.add(x)
            
#             for i in range(n):
#                 x ^= (1 << i)
#                 if x not in seen:
#                     backtrack(x)
#                 x ^= (1 << i)
                
#         backtrack()
#         return ans       
                
