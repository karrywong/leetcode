class Solution:
    def firstUniqChar(self, s: str) -> int:
        # soln 1
        seen = {}
        for i, e in enumerate(s):
            if e in seen:
                seen[e] = float('inf')
            else:
                seen[e] = i  
        ans = min(seen.values())
        return ans if ans != float('inf') else -1
            
                
        
​
