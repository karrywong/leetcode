class Solution:
    def simplifyPath(self, path: str) -> str:
        #LeetCode soln, clean, time O(N), space O(N)
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p == "." or not p:
                continue
            else:
                stack.append(p)
        return "/"+"/".join(stack)
        
#         #First attempt, code messy, time O(N), space O(N)
#         stack = ['/']
#         i = 0
        
#         while i < len(path):
#             if path[i] == '/':
#                 if stack and stack[-1] != '/':
#                     stack.append(path[i])
#             elif path[i] == "." and stack[-1] == "/":
#                 count = 1
#                 while i+1 < len(path) and path[i+1] == ".":
#                     count += 1
#                     i += 1
#                 if (i+1 < len(path) and path[i+1] != "/") or count >= 3:
#                     stack.append("."*count)
#                 elif count == 2:
#                     if len(stack) > 1 and stack[-1] == "/":
#                         stack.pop()
#                         while stack and stack[-1] != '/':
#                             stack.pop()
#             else:
#                 stack.append(path[i])
#             i += 1
#         return ''.join(stack[:-1]) if len(stack) > 1 and stack[-1] == '/' else ''.join(stack)
