class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = [l for l in s.lower() if l.isalnum()]
        temp = "".join(temp)
        return temp[::-1] == temp
​
