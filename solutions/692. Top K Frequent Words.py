class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #Soln by is_1337, brilliant, time O(Nlogk), space O(N) w N = len(words)
        count = collections.Counter(words)        
        return heapq.nsmallest(k, count.keys(), key=lambda x : (-count[x],x)) 
