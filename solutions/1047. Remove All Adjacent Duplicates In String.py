class Solution:
    def removeDuplicates(self, s: str) -> str:
        #Straight-forward stack, time O(N), space O(N)
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
