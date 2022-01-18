class Solution:
    def maxProduct(self, words: List[str]) -> int:
#         #LeetCode soln 1 optimize no common letters comparsion, time O(N^2+L), space O(N)
#         n = len(words)
#         masks = [0]*n
        
#         for i in range(n): #Construct bit mask for each word
#             bit_mask = 0
#             for char in words[i]:
#                 bit_mask |= 1 << (ord(char)-ord('a'))
#             masks[i] = bit_mask
        
#         ans = 0
#         for i in range(n):
#             for j in range(i+1,n):
#                 if masks[i] & masks[j] == 0:
#                     ans = max(ans, len(words[i]) * len(words[j]))
#         return ans
        
        #LeetCode soln 2 further optimize with hashmap to keep the max string length for the same bitmask
        hashmap = collections.defaultdict(int)
        for word in words:
            bit_mask = 0
            for char in word:
                bit_mask |= 1 << (ord(char)-ord('a'))
            hashmap[bit_mask] = max(hashmap[bit_mask], len(word))
        
        ans = 0
        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    ans = max(ans, hashmap[x]*hashmap[y])
        return ans
