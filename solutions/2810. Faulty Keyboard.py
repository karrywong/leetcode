class Solution:
    def finalString(self, s: str) -> str:
        ans = deque([])
        left_to_right:bool = True
        for char in s:
            if char == "i":
                left_to_right = not left_to_right
                continue
            
            if left_to_right:
                ans.append(char)
            else:
                ans.appendleft(char)
                
        if not left_to_right: ans.reverse()
        return "".join(ans)
