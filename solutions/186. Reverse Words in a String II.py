class Solution:
​
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        left = 0
        
        for i in range(0, len(s)):
            if s[i] == " ":
                right = i - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -=1 
                left = i + 1
            if i == len(s) - 1:
                right = len(s) - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -=1                 
