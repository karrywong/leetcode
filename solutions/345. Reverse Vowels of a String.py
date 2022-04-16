class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels += [char.upper() for char in vowels]
        indices = [i for i, char in enumerate(lst) if char in vowels]
        for k in range(len(indices)//2):
            a, b = indices[k], indices[~k]
            lst[a], lst[b] = lst[b], lst[a]
        return ''.join(lst)
