class Solution:
    def minSwaps(self, s: str) -> int:
        # #Failed to convert hints into answer, inspired by lucliu in discussion
        # #Time O(N), space O(1)
        # ans, l, r = 0, 0, 0
        # for i in range(len(s)):
        #     if s[i] == "[":
        #         l += 1
        #     else:
        #         r += 1
        #     if r > l:
        #         ans += 1
        #         l += 1
        #         r -= 1
        # return ans
    
        #Even simpler soln by inasaaone in discussion, time O(N), space O(1)
        count_openBracket = 0
        for char in s:
            if char == '[':
                count_openBracket += 1
            elif count_openBracket:
                count_openBracket -= 1
        return (count_openBracket+1) // 2
