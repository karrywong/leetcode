class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ### Soln - sorting with key as library
        lib = {v: i for i, v in enumerate(order)}
        return words == sorted(words, key = lambda x : [lib[x[i]] for i in range(len(x))])
​
        
        
