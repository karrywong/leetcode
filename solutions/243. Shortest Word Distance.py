class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        #soln 1 - Leetcode One-pass, Time O(N), Space O(1)
        i, j = -1, -1
        mindist = len(wordsDict)
        for k, word in enumerate(wordsDict):
            if word1 == word:
                i = k
            elif word2 == word:
                j = k
            if i != -1 and j != -1:
                mindist = min(mindist, abs(i-j))
        return mindist
                
        #soln 0 - first attempt, Time O(N^2), Space O(1)
#         lst1, lst2 = [], []
#         for i, word in enumerate(wordsDict):
#             if word == word1:
#                 lst1.append(i)
#                 continue
#             if word == word2:
#                 lst2.append(i)
        
#         ans = len(wordsDict) - 1
#         for i in lst1:
#             for j in lst2:
#                 ans = min(abs(i-j),ans)
#         return ans
                
        
