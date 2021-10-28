class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #soln 0, first attempt, Time: O(N) and Space O(N) where N is the length of magazine
        m = len(ransomNote)
        n = len(magazine)
        if m > n: 
            return False
        lib = collections.Counter(magazine)
        
        for r in ransomNote:
            if r not in lib:
                return False
            else:
                lib[r] -= 1
                if lib[r] == 0:
                    del lib[r]
        return True
        
        
