class Solution:
    def reverseVowels(self, s: str) -> str:
        #Stefan Pochmann
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
        
        # #Time O(N), space O(N), straight forward
        # lst = list(s)
        # vowels = ['a', 'e', 'i', 'o', 'u']
        # vowels += [char.upper() for char in vowels]
        # indices = [i for i, char in enumerate(lst) if char in vowels]
        # for k in range(len(indices)//2):
        #     a, b = indices[k], indices[~k]
        #     lst[a], lst[b] = lst[b], lst[a]
        # return ''.join(lst)
