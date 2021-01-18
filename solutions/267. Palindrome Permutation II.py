class Solution:
    def generatePalindromes(self, s: str) -> List[str]:        
        ### Soln 1 - use itertools.permutations - time exceeded since we check all possible permutation  
        counts = collections.Counter(s)
        check = [l for l,f in counts.items() if f % 2 == 1]
        if len(check) > 1: return []
        
        if len(counts.items()) == 1:
            return ["".join(s)]
​
        lst = []
        for c, v in counts.items():
            lst.extend(c * (v//2))
        all_perm = set(itertools.permutations(lst))
​
        res = []
        if len(check) == 0:
            return ["".join(a + a[::-1]) for a in all_perm]
        else:
            return ["".join(a + tuple(check[0]) + a[::-1]) for a in all_perm]
        
        
            
        
                
            
            
            
            
