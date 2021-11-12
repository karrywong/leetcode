class Solution:
    def isValid(self, s: str) -> bool:
        #From sielicki in Discussion
        while 'abc' in s:
            s = s.replace('abc', '')
        return len(s) == 0
        
        # #soln 1 - second attempt w/o recursion
        # while s:
        #     if len(s) == 0: return True
        #     if len(s) < 3: return False
        #     if len(s) == 3:
        #         if s == "abc": return True
        #         else: return False
        #     temp = s
        #     for i in range(len(s)):
        #         if s[i:i+3] == "abc":
        #             s = s[:i] + s[i+3:]
        #             break
        #     if temp == s: return False    
        
        #soln 0 - first attempt w recursion
        # if len(s) < 3: return False
        # if len(s) == 3: 
        #     if s == "abc": return True
        #     else: return False
        # i = 0
        # while i < len(s):
        #     if s[i:i+3] == "abc":
        #         return self.isValid(s[:i] + s[i+3:])
        #     i += 1
        # return False
