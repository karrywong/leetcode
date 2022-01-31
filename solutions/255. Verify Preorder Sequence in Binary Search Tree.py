class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        #Totally stucked, idea from muleax in discussion
        #Time O(N), Space O(N)
        lo = float('-inf')
        stack = []
        
        for val in preorder:
            if val < lo:
                return False
            while stack and stack[-1] < val:
                lo = stack.pop()
            stack.append(val)
        return True
​
#         #Optimized, time O(N), Space O(1)
#         lo = float('-inf')
#         hi = float('-inf')
        
#         for i, val in enumerate(preorder):
#             if val < lo:
#                 return False
            
#             if val > hi: 
#                 lo = hi
#                 hi = val
#             else:
#                 j = i-1
#                 while j >= 0 and val > preorder[j]:
#                     lo = preorder[j]
#                     j -= 1
#         return True
