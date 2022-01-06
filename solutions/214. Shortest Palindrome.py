class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #Mock interview practice, not successful, key idea is hash function
        #there is always a solution. Worst case: "s0...sn" -> "sn sn-1 ... s0... sn"
        #1. find longest palindromic substring starting from index 0, "aacecaaa" -> "aacecaa"
        #s = "cbabcd" , rev = "dcbabc" -> s + "#" + rev = "cbabcd#dcbabc"
        
        # #Brute force O(N^2) as the starting point
        # rev = s[::-1]
        # for i in range(len(s)):
        #     if s[:len(s)-i] == rev[i:]:
        #         return rev[:i] + s
        # return ""
        
        #Optimized, key idea is Knuth–Morris–Pratt algorithm
        rev = s[::-1]
        s_new = s + "#" + rev
        n_new = len(s_new)
        f = [0]*n_new
        for i in range(1,n_new):
            t = f[i-1]
            while (t > 0 and s_new[i] != s_new[t]):
                t = f[t-1]
            if s_new[i] == s_new[t]:
                t += 1
            f[i] = t
        print(f[n_new-1])
        return rev[:len(rev)-f[n_new-1]] + s
    
        #eg1, s+"#"+rev = "aacecaaa#aaacecaa", f[n_new-1] = 7
