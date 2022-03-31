class WordDistance:
    #lookup = {} #key: word, values: list[indices] (sorted) 
    #list1 = [4,5,7], list2 = [1,8,10], no common element
    #two pointers - i,j -> option (1) O(len(list1)+len(list2)), 
    # option (2) binary search, loop over list2, bisect -> compute distance, time O(len(list2)* log(len(list1)))
    
    #M = len(list1), N = len(list2), WLOG M > N
    #option 1, O(M)
    #option 2, O(NlogM)
    
    #list1 = [4,7], list2 = [1,3,5]
    
    def __init__(self, wordsDict: List[str]):
        self.lookup = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.lookup[word].append(i)
​
    def shortest(self, word1: str, word2: str) -> int:
        i, j = 0, 0
        M, N = len(self.lookup[word1]), len(self.lookup[word2]) #M, N > 0 
        ans = float('inf')
        while i < M and j < N:
            if self.lookup[word1][i] < self.lookup[word2][j]:
                ans = min(ans, self.lookup[word2][j]-self.lookup[word1][i])
                i += 1
            else:
                ans = min(ans, self.lookup[word1][i]-self.lookup[word2][j])
                j += 1
        return ans
​
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
