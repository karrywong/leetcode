class Solution:
    def validPalindrome(self, s: str) -> bool:
        ### Soln 2 Greedy algorithm, LeetCode solution
        def is_pali_range(i,j):
            return all(s[k] == s[j-k+i] for k in range(i,j))
​
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1,j) or is_pali_range(i, j-1)
        return True
        
        ### Soln 1 - brute force, time exceeded
        # for i in range(len(s)):
        #     temp = [l for j, l in enumerate(s) if j != i]
        #     if temp == temp[::-1]: 
        #         return True
        # return False
        
