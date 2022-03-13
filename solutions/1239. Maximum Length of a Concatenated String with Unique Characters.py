class Solution:
    def maxLength(self, arr: List[str]) -> int:
        #Time: O(2**n), n = length of all strings with unique character
        #arr2 = ["abcd", "efgz", "ehx", "fiy"]
        lookup = {}
        for string in arr:
            checker = 0
            for char in string:
                val = 1 << (ord(char) - ord('a'))
                if checker & val != 0:
                    break
                checker |= val
            else: #string consists of unique characters
                lookup[string] = checker
        
        arr2 = sorted(lookup.keys(),reverse = True, key = len) #at most arr
        ans = 0 
        
        def dfs(ind: int, S: str):
            nonlocal ans
            ans = max(ans, len(S))
            
            for i in range(ind+1, len(arr2)):
                if lookup[S] & lookup[arr2[i]] == 0:
                    lookup[S+arr2[i]] = lookup[S] | lookup[arr2[i]]
                    dfs(i, S+arr2[i])
            
        for i, string in enumerate(arr2):
            dfs(i, string) 
        return ans
