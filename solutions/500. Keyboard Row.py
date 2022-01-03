class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #Brute force, time O(W), space O(1), where W is total number of letters in words
        keyboard = {"qwertyuiop", "asdfghjkl", "zxcvbnm"}
        lookup = []
        for row in keyboard:
            lookup.append(set([r for r in row]))
        
        ans = []
        for word in words:
            for check in lookup:
                temp = word.lower()
                if all([l in check for l in temp]):
                    ans.append(word)
        return ans
​
#         #Inspired by uds5501 in discussion, alternative
#         lookup = [['q','w','e','r','t','y','u','i','o','p'], \
#                   ['a','s','d', 'f', 'g', 'h', 'j', 'k', 'l'], \
#                   ['z','x','c', 'v', 'b', 'n', 'm']]
        
#         ans = []
#         for word in words:
#             lier = [False, False, False]
#             for letter in word: 
#                 for i in range(3): 
#                     if letter.lower() in lookup[i]:
#                         lier[i] = True
#             if sum(lier) == 1:
#                 ans.append(word)
#         return ans
