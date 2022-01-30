class Solution:        
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        #Robin-Karp algorithm, constant time rolling hash, time O(N), space O(1)
        #inspired by h00p3r2, idea is that calculating the hash code of s[i: i + k] from s[i + 1: i + 1 + k] is easy
        #because HASH(s[i: i + k]) = p * ( HASH(s[i + 1: i + 1 + k]) - s[i + k]) + s[i].
        n, val, ans = len(s), 0, ""
        lookup = {}
        for char in string.ascii_lowercase:
            lookup[char] = ord(char)-ord('a')+1
        
        pkMinusOne = 1
        for j in range(k-1):
            pkMinusOne = (pkMinusOne*power) % modulo
        
        val = 0
        for i in range(n-k,-1,-1):
            sub = s[i:i+k]
            if i == n-k:
                v = 1
                for i in range(len(sub)):
                    val = (val + (lookup[sub[i]]*v) %modulo) %modulo
                    v = (v*power) % modulo
            else:
                val = (val-lookup[s[i+k]]*pkMinusOne) % modulo
                val = (val*power) % modulo
                val = (val+lookup[s[i]]) %modulo
            if val == hashValue:
                ans = sub
        return ans
