class Solution:
    def frequencySort(self, s: str) -> str:
        # #soln 0 - Hashtable, two-liner, Time O(NlogN), Space O(N)
        # lib = collections.Counter(s)
        # return ''.join([ k*v for k, v in sorted(lib.items(), key = lambda x : x[1], reverse = True)])
        
        #soln 1 - BucketSort, time O(N), space O(N)
        lib = collections.Counter(s) #O(n)
        max_freq = max(lib.values())
        buckets = [[] for _ in range(max_freq+1)]
        
        for letter,freq in lib.items():
            buckets[freq].append(letter)  #O(k)
        
        return "".join([freq*letter for freq in range(max_freq,0,-1) for letter in buckets[freq]])
            
        
