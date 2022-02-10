class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # #soln 2 - DP, tricky idea, time O(N^3), space O(N)
        # word_set = set(wordDict)
        # dp = [False] * (len(s) + 1)
        # dp[0] = True #null string
        # for i in range(1, len(s) + 1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in word_set:
        #             dp[i] = True
        #             break
        # return dp[len(s)]
        
#         #soln 1 - recursion with memoization top-down, time O(N^3), space O(N)
#         lib = {x : True for x in wordDict} #"xyz": True/False
#         def helper(remainder):
#             if remainder in lib:
#                 return lib[remainder]
            
#             for word in wordDict:
#                 if len(remainder) > len(word) and remainder.endswith(word):
#                     x = remainder[:-len(word)]
#                     lib[x] = helper(x)
#                     if helper(x): 
#                         return True
#             return False
        
#         return helper(s)
                
        #soln 0 - second attempt, BFS intuitive 
        n = len(s)
        word_set = set(wordDict)
        queue = collections.deque([0])
        seen = set()
        while queue: #BFS
            start = queue.popleft()
            if start == n:
                return True
            if start in seen:
                continue
            for end in range(start+1, n+1):
                if s[start:end] in word_set:
                    queue.append(end)
            seen.add(start)
        return False
