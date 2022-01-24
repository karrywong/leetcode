class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        #main idea: use heap, time O(NlogN)
        IDs = {} #key: ID, value: heap
        for ID, score  in items: #O(N), N = len(items)
            if ID not in IDs:
                lst = [-1*score]
                heapq.heapify(lst)
                IDs[ID] = lst
            else:
                heapq.heappush(IDs[ID], -1*score) #O(logN)
        
        ans = []
        for ID in sorted(IDs): #len(IDs) <= N
            val = 0
            for _ in range(5):
                val += -1*heapq.heappop(IDs[ID]) #O(logN)
            ans.append([ID, val//5])
        return ans
                
