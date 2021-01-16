class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_R = count_L = 0
        res = 0
        
        for l in s:
            if l == 'R':
                count_R += 1
            else:
                count_L += 1
            
            if count_R == count_L:
                res += 1
        return res
