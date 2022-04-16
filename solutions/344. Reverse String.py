class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # #soln 1 - n/2 swaps
        l = len(s)
        for i in range(0, l//2):
            s[i], s[~i] = s[~i], s[i]
            
        # #soln 0 - built-in ft
        # s.reverse()
            
