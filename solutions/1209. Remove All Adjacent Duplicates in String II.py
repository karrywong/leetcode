class Solution:
    # recent attempt, Time O(N), space O(N)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for idx, cur_char in enumerate(s):
            if stack and stack[-1][0] == cur_char:
                prev_char, freq = stack.pop()
                if freq+1 < k:
                    stack.append((prev_char, freq+1))
            else:
                stack.append((cur_char,1))
        return "".join([char * freq for char, freq in stack])
                        
                    
