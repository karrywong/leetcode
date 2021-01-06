class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ## Soln 1 - LeetCode (no successful attempt on my own)
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
​
        return j == len(popped)
        
        ### Soln 2 - by silvergalleon in discussion
#         stack, i = [], 0
        
#         for n in pushed:
#             stack.append(n)
#             while stack and stack[-1] == popped[i]:
#                 stack.pop()
#                 i += 1
        
#         while i < len(popped):
#             if not stack or stack[-1] != popped[i]:
#                 return False
#             stack.pop()
