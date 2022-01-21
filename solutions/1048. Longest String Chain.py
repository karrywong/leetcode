class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #Failed attempt, Leetcode top-down DP
        #Time O(N+N*L^2) = O(N*L^2), space O(N)
        wordsPresent = set(words)
        memo = {} #key: word, value: integer, eg ab->a w/ memo[ab]=2
​
        def dfs(w): # find the longest word sequence
            if w in memo:
                return memo[w]
            
            maxLength = 1
            for i in range(len(w)):
                temp = w[:i] + w[i+1:]
                if temp in wordsPresent:
                    curLength = 1 + dfs(temp)
                    maxLength = max(maxLength, curLength)
            memo[w] = maxLength
            return maxLength
                
        ans = 0
        for word in words:
            ans = max(ans, dfs(word))
        return ans
