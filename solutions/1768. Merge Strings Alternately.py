class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #one-liner by kamanashisroy using zip_longest
        return ''.join(map(lambda a:a[0]+a[1],zip_longest(word1,word2,fillvalue='')))
    
        # #Two pointers, straightforward, time O(N+M), space O(N+M)
        # i, j = 0,0
        # ans = ""
        # while i < len(word1) and j< len(word2):
        #     ans += word1[i] + word2[j]
        #     i += 1
        #     j += 1
        # return ans + word1[i:] if j == len(word2) else ans + word2[j:]
