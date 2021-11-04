class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]: 
        #soln 0 - backtracking, Time O(k * nCk), Space O(nCk)
        ans = []
        def backtrack(start, A=[]):
            if len(A) == k:
                ans.append(A[:])
                return
            
            for i in range(start,n+1):
                A.append(i)
                backtrack(i+1,A)
                A.pop()
        
        backtrack(1)
        return ans
        
        # #Extra - Leetcode lexicographic (binary sorted) combinations
        # nums = list(range(1, k+1)) + [n+1]
        # ans, j = [], 0
        # while j < k:
        #     ans.append(nums[:k])
        #     j = 0
        #     while j < k and nums[j+1]==nums[j]+1:
        #         nums[j] = j + 1
        #         j += 1
        #     nums[j] += 1
        # return ans
