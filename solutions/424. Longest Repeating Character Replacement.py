class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #brute force: loop over A-Z versus Choose most frequent character O(N)    
        #"ABCCAA" -> Counter = {"A":3, "B":1, "C":2} (or arr = [3, 0, ..., 0])
        #Counter["A"] -= 1
    
        #AABBC.. 
        
        counter = collections.Counter()
        ans = 0
        l = 0
        cnt = 0 #count frequency of non-char alphabets
        for r in range(len(s)):
            counter[s[r]] += 1
            if r == 0 or counter[s[r]] > counter[char]:
                char = s[r]
                
            if s[r] != char:
                cnt += 1
                
            while cnt > k:
                counter[s[l]] -= 1 
                if s[l] != char:
                    cnt -= 1
                else:
                    char = max(counter, key = counter.get) #O(1)
                    cnt = r-l-counter[char]
                l += 1
            
            # print(r, l, counter, char, ans)
            ans = max(ans, r - l + 1)
            
        return ans
