class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ### Soln 1 - Leetcode Sliding window + Hashmap
        n1, n2 = len(s1), len(s2)
        if n1 > n2 : return False
        
        lib1 = collections.Counter()
        lib2 = collections.Counter()
        for i in range(n1):
            lib1[s1[i]] += 1
            lib2[s2[i]] += 1
        
        for i in range(n2 - n1):
            if lib1 == lib2:
                return True
            lib2[s2[i + n1]] += 1
            lib2[s2[i]] -= 1
            if lib2[s2[i]] == 0:
                del lib2[s2[i]]
                
        return lib1 == lib2
