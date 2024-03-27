class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        # referenced kebetsi, time O(n*2^n), space O(N)
        ans = []
        def backtrack(arr:List[str]=[], ind:int=0):
            if ind == len(word):
                ans.append(''.join(arr[:]))
                return
            
            # we abbreviate if it's the start or if the last character is a letter
            if len(arr) == 0 or arr[-1].isalpha():
                # abbreviate the next i letters
                for i in range(ind+1,len(word)+1):
                    backtrack(arr + [str(i-ind)], i)
                    
            # in any case, we also have a path where we don't abbreviate
            # backtrack(arr + [word[-left]], left-1)
            backtrack(arr + [word[ind]], ind+1)
            
        backtrack()
        return ans
