from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # len(word1) != len(word2) -> False
        # example 1: {a:1, b:1, c:1}, {a:1, b:1, c:1} -> True
        # example 3: {a:2, b:3, c:1}, {a:1, b:2, c:3} -> True
        # {a:2, b:3, c:1} -> {a:2, b:1, c:3} -> {a:1, b:2, c:3}
        
        # {a:2, b:2, c:1}, {a:1, b:2, c:2} -> True
        # lookup = {2:2, 1:1}
        # {a:3, b:3, c:1}, {a:1, b:4, c:2} -> False
        
        # Time O(N), N=len(word), space O(1)
        if len(word1) != len(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        if count1.keys() != count2.keys():
            return False
        
        lookup = defaultdict(int)
        for v in count1.values():
            lookup[v] += 1
        
        for v in count2.values():
            lookup[v] -= 1
            
        for v in lookup:
            if lookup[v] != 0:
                return False
        return True
        
        
        
      
