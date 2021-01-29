class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        # ### Soln 0
        tbl = {v : i for i,v in enumerate(B)}
        return [tbl[w] for w in A]
