class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        #Two-liner by ye15, time O(N), space O(1)
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]
        
        # #First attempt w/ one swap, time: O(N), space O(1)
        # if len(s1) != len(s2): return False        
        # once = False
        # swap = []
        # for char1, char2 in zip(s1, s2):
        #     if char1 != char2:
        #         if once: return False
        #         if not swap:
        #             swap.extend([char1,char2])
        #         elif swap[0] != char2 or swap[1] != char1:
        #             return False
        #         else:
        #             once = True
        #             swap = []
        # return False if swap else True
            
        
