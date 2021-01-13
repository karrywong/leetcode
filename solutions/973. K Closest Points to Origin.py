class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ### Soln 1 - Hashmap O(n)
        lib = {}
        
        for n in points:
            dist = n[0]**2 + n[1]**2
            if dist not in lib:
                lib[dist] = [n]
            else:
                lib[dist].append(n)
                
        res = []
        lst = [v for v in sorted(lib.keys())]
        i = 0
        while K > 0: 
            k = lst[i]
            val = len(lib[k])
            res += lib[k]
            
            K -= val
            i += 1
            
        return res
