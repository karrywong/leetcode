class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        #Totally stuck, soln inspired by AlexSzeto and Vlad, sliding window 
        #Time O(26*n)~O(n), space O(1)
        if count > len(s):
            return 0 
        ans = 0
        ub_unique = 1+min(len(s) // count, len(set(s)))
        
        for target in range(1, ub_unique):
            seen = collections.Counter() #sliding window
            has_count = 0
            for i, char in enumerate(s):
                seen[char] += 1
                has_count += seen[char] == count
                if count * target <= i:
                    prev_char = s[i-count * target]
                    has_count -= seen[prev_char] == count
                    seen[prev_char] -= 1
                ans += has_count == target
        return ans
​
#         #Totally stuck, soln inspired by AlexSzeto, sliding window 
#         #Time O(26*n)~O(n), space O(1)
#         if count > len(s):
#             return 0 
#         ans = 0
#         ub_unique = 1+min(len(s) // count, len(set(s)))
        
#         for target in range(1, ub_unique):
#             seen = collections.Counter() #sliding window
#             l = 0 
#             for char in s:
#                 seen[char] += 1
                
#                 while len(seen) > target or seen[char] > count:
#                     seen[s[l]] -= 1
#                     if seen[s[l]] == 0: del seen[s[l]]
#                     l += 1
                
#                 if len(seen) == target and all(val == count for val in seen.values()):
#                     ans += 1
#         return ans       
