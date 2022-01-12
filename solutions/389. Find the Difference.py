class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #Bit manipulation, time O(N), space O(1)
        if len(t) == 1: 
            return t
        bit = ord(t[0])
        for char1, char2 in zip(s,t[1:]):
            bit ^=  ord(char1) ^ ord(char2)
        return chr(bit)
        
#         #Hash table, time O(N), space O(1) due to the fixed number of a-z letters
#         htb = collections.Counter(s)
#         for char in t:
#             if char not in htb:
#                 return char
            
#             htb[char] -= 1
#             if htb[char] == 0:
#                 del htb[char]
