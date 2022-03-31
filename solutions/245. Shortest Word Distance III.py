class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        #Almost identical to #244. Shortest Word Distance II
        lookup = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            lookup[word].append(i)
        if word1 == word2:
            n = len(lookup[word1])
            ans = lookup[word1][1]-lookup[word1][0]
            for i in range(1,n-1):
                ans = min(ans, lookup[word1][i+1]-lookup[word1][i])
            return ans
        else:
            i, j = 0, 0
            M, N = len(lookup[word1]), len(lookup[word2]) #M, N > 0 
            ans = float('inf')
            while i < M and j < N:
                if lookup[word1][i] < lookup[word2][j]:
                    ans = min(ans, lookup[word2][j]-lookup[word1][i])
                    i += 1
                else:
                    ans = min(ans, lookup[word1][i]-lookup[word2][j])
                    j += 1
            return ans
