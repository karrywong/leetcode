class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # soln 1 - backtracking, Time O(N*4^N), Space O(N)
        ans = []
        if not digits: return ans
        lib = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", \
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(index, path=[]):
            if len(path) == len(digits):
                ans.append(''.join(path))
                return
            
            letters = lib[digits[index]]
            for e in letters:
                path.append(e)
                backtrack(index+1, path)
                path.pop()
        
        backtrack(0)
        return ans
        
#         # soln 0 - naive iteration
#         lib = {"2": ("a", "b", "c"), "3": ("d", "e", "f"), "4": ("g", "h", "i"), \
#                "5": ("j", "k", "l"), "6": ("m", "n", "o"), "7": ("p", "q", "r", "s"), 
#                "8": ("t", "u", "v"), "9": ("w", "x", "y", "z")}
#         ans = []
#         if not digits: 
#             return ans
#         else: 
#             ans = [e for e in lib[digits[0]]]
        
#         for i in range(1,len(digits)):
#             tp = lib[digits[i]]
#             temp, ans = ans, []
#             for t in temp:
#                 for j in range(len(tp)):
#                     ans.append(t + tp[j])
#         return ans
