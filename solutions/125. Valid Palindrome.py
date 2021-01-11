class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = [l for l in s if l.isalnum()]
        temp = "".join(temp)
        return temp[::-1] == temp
​
