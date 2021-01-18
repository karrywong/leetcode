class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ### Soln 3 - one fly, clever idea
        lib = {}
        count = 0
        for k in s:
            if k not in lib:
                lib[k] = 1
            else:
                lib[k] += 1
            
            if lib[k] % 2 == 0:
                count -= 1
            else:
                count += 1
            
        return count <= 1
        
        ### Soln 2 - one-liner by andreacolo737 in discussion
        # return sum([s.count(x) % 2 != 0 for x in set(s)]) <= 1
        
        # ### Soln 1 - first attempt, hashmap
        # counts = collections.Counter(s)
        # lst = [x for x in counts.values() if x % 2 == 1]
        # return True if len(lst) <= 1 else False
