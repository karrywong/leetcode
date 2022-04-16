class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        lst = list(s)
        for i in range(len(s)-1,-1,-1):
            if lst[i] in vowels:
                lst.pop(i)
        return ''.join(lst)
