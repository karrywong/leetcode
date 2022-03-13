class Solution:
    def firstUniqChar(self, s: str) -> int:
        #two sweeps, first, arr[char] += 1
        #second sweep return first non-repeating
        #Time O(N), space O(1)
        arr = [0] * 26
        a_ascii = ord('a')
        for char in s:
            arr[ord(char)-a_ascii] += 1
        for i, char in enumerate(s):
            if arr[ord(char)-a_ascii] == 1:
                return i
        return -1
    
        # #Old attempt 
        # count = collections.Counter(s)
        # for idx, ch in enumerate(s):
        #     if count[ch] == 1:
        #         return idx  
        # return -1        
