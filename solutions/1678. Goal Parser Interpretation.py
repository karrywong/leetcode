class Solution:
    def interpret(self, command: str) -> str:
        #Second attempt, one-liner
        return command.replace('()','o').replace('(al)','al')        
        
        # #First attempt, straightforward, time O(N), space O(N), where N = len(command)
        # stack = []
        # for char in command:
        #     if stack and stack[-1] == "(" and char == ")":
        #         stack.append("o")
        #     else:
        #         stack.append(char)
        # return ''.join([char for char in stack if char not in ("(", ")")])
