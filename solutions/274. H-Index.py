class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #Mock interview with Haotian
        #[5,5,3,1,0]
        #sort in reversed order
        #ind, citation in enumerate(), possible if 
        # 1 cond: citation <= ind+1 (no of papers)
        # 2 cond: citations[-citation] <= citation
        
        #[3,1,1]
        # ind = 1, citation = 1, 1st cond yes, 2nd cond yes, return citation
​
        #[0] or [0,0,0...], true answer = 0
        #[7], true answer = 1
        #[7,6], true answer = 2
        #[7,6,5,5], true answer = 4
        #[2,2,4], true answer=2
        #[2,4,4,4] -> [4,4,4,2], true answer = 3
        
#         #answer must be in range of [0, len(citations)]
#         citations.sort(reverse=True)
#         n = len(citations)
#         #corner case
#         if citations[-1] >= n:
#             return n
        
#         for h in range(n-1, -1, -1):
#             if citations[h-1] >= h and citations[h] <= h:
#                 return h         
       
        #LeetCode solution
        citations.sort()
        i = 0
        n = len(citations)
        while i < n and citations[n-1-i] > i:
            i += 1
        return i 
