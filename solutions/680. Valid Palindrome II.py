class Solution:
    def validPalindrome(self, s: str) -> bool:
        ### Soln 3 Greedy algorithm, simpler from discussion by MAaRNG
        # if s == s[::-1]:
        #     return True
        # for i in range(len(s)-1):
        #     if s[i] != s[-i-1]:
        #         return s[i: -i-2] == s[i+1: -i-1][::-1] or s[i+1: -i-1] == s[i+2: len(s)-i][::-1]
        # return False     
        
#         ### Soln 2 Greedy algorithm, LeetCode solution
        # def is_pali_range(i,j):
        #     return all(s[k] == s[j-k+i] for k in range(i,j))
​
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                # return is_pali_range(i+1,j) or is_pali_range(i, j-1)
                return s[i+1:j+1] == s[i+1:j+1][::-1] or s[i:j] == s[i:j][::-1]
        return True
        
        ### Soln 1 - brute force, time exceeded
        # for i in range(len(s)):
        #     temp = [l for j, l in enumerate(s) if j != i]
        #     if temp == temp[::-1]: 
        #         return True
        # return False
        
