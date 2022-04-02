class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        letters1 = collections.Counter(s1)
        letters2 = collections.Counter(s2)
        if len(letters1) != len(letters2): return False
        
        once = False
        swap = []
        for char1, char2 in zip(s1, s2):
            if char1 != char2:
                if once: return False
                if not swap:
                    swap.extend([char1,char2])
                elif swap[0] != char2 or swap[1] != char1:
                    return False
                else:
                    once = True
                    swap = []
        return False if swap else True
            
        
