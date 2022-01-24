class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        #smart soln by EklavyaJoshi in discussion
        if len(sequence) < len(word):
            return 0
        x = 0
        while True:
            if word*(x+1) in sequence:
                x += 1
            else:
                return x
