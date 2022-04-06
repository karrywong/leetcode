class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #First atteempt, straightforward
        lookup = {}
        for i, char in enumerate(order):
            lookup[char] = i
        
        for j in range(len(words)-1):
            word1, word2 = words[j], words[j+1]
            x = 0
            n = min(len(word1), len(word2))
            while x < n:
                if lookup[word1[x]] > lookup[word2[x]]:
                    return False
                elif lookup[word1[x]] < lookup[word2[x]]:
                    break
                x += 1
            if x < n:
                continue
            elif word1[n:]:
                return False
        return True
