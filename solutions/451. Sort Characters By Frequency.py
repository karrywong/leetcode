class Solution:
    def frequencySort(self, s: str) -> str:
        #soln 0 - first attempt, two-liner, Time O(NlogN), Space O(N)
        lib = collections.Counter(s)
        return ''.join([ k*v for k, v in sorted(lib.items(), key = lambda x : x[1], reverse = True)])
        
        
