class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # #soln 1 - Leetcode build string
        # def build(string):
        #     ans = []
        #     for ele in string:
        #         if ele != "#":
        #             ans.append(ele)
        #         elif ans:
        #             ans.pop()
        #     return "".join(ans)
        # return build(s) == build(t)
        
        #first attempt failed, then modified
        i, j = 0, 0
        stack1, stack2 = [], []
        for i in range(len(s)):
            if s[i] != "#":
                stack1.append(s[i])
            elif stack1:
                stack1.pop()
        
        for j in range(len(t)):
            if t[j] != "#":
                stack2.append(t[j])
            elif stack2:
                stack2.pop()
        return True if stack1 == stack2 else False
