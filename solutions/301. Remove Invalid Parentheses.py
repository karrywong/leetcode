class Solution:
#     # Pretty stuck, looked at Leetcode backtracking soln 2, Time O(2^N), space O(N)
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = 0,0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                right += 1 if left == 0 else 0
                left -= 1 if left > 0 else 0
                
        result = set()
        def recurse(string, index=0, left_count=0, right_count=0, left_rem=left, right_rem=right, expr=[]):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    result.add("".join(expr))
            else:
                cur_char = string[index]
                if (cur_char == '(' and left_rem > 0):
                    recurse(s, index+1, left_count, right_count, left_rem-1, right_rem, expr)
                elif(cur_char == ')' and right_rem > 0):
                    recurse(s, index+1, left_count, right_count, left_rem, right_rem-1, expr)
                expr.append(cur_char)
                
                if cur_char != '(' and cur_char != ')':
                    recurse(s, index+1, left_count, right_count, left_rem, right_rem, expr)
                elif cur_char == '(':
                    recurse(s, index+1, left_count+1, right_count, left_rem, right_rem, expr)
                elif cur_char == ')' and left_count > right_count:
                    recurse(s, index+1, left_count, right_count+1, left_rem, right_rem, expr)
                expr.pop()
        recurse(s)  
        return list(result)
    
#     #Leetcode backtracking soln 1, Time O(2^N), space O(N)
#     def __init__(self):
#         self.valid_expressions = set()
#         self.min_removed = float("inf")
#     """
#         string: The original string we are recursing on.
#         index: current index in the original string.
#         left: number of left parentheses till now.
#         right: number of right parentheses till now.
#         ans: the resulting expression in this particular recursion.
#         ignored: number of parentheses ignored in this particular recursion.
#     """
#     def remaining(self, string, index=0, left_count=0, right_count=0, expr=[], rem_count=0):
#         if index == len(string):
#             if left_count == right_count:
#                 if rem_count <= self.min_removed:
#                     possible_ans = "".join(expr)
#                     if rem_count < self.min_removed:
#                         self.valid_expressions = set()
#                         self.min_removed = rem_count
#                     self.valid_expressions.add(possible_ans)
#         else:
#             cur_char = string[index]
#             if cur_char != '(' and cur_char != ')':
#                 expr.append(cur_char)
#                 self.remaining(string, index+1, left_count, right_count, expr, rem_count)
#                 expr.pop()
#             else:
#                 self.remaining(string, index+1, left_count, right_count, expr, rem_count+1)
#                 expr.append(cur_char)
#                 if cur_char == '(':
#                     self.remaining(string, index+1, left_count+1, right_count, expr, rem_count)
#                 elif right_count < left_count:
#                     self.remaining(string, index+1, left_count, right_count+1, expr, rem_count)
#                 expr.pop()
                    
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         self.remaining(s)
#         return list(self.valid_expressions)
