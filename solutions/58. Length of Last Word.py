class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # #First attempt, time O(N), space O(1)
        # s = s.rstrip()
        # count = 0
        # ptr = len(s) - 1
        # while ptr >= 0 and s[ptr] != " ":
        #     count += 1
        #     ptr -= 1
        # return count
        
        #Second attempt, time O(N), space O(1)
        s = s.split()
        return len(s[-1])
