class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #Optimized, Monotonic Stack, time O(N), space O(1)
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        finalStack= stack[:-k] if k else stack
        return "".join(finalStack).lstrip("0") or "0"
        
#         #First attempt, greedy, time O(N^2), space O(1)
#         def helper(s): #to remove one digit st it becomes smallest possible
#             if len(s) == 1:
#                 return "0"
#             i = 0
#             while i < len(s)-1:
#                 if s[i] > s[i+1]:
#                     break
#                 i += 1
#             s = s[:i]+s[i+1:]
#             return s.lstrip("0") if i == 0 else s
​
#         for _ in range(k):
#             num = helper(num)
#             if not num or num == "0":
#                 return "0"
#         return num
