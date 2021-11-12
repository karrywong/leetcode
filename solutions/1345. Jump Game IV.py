class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #soln 1 - leetcode bidirectional BFS
        n = len(arr)
        if n == 1: return 0
        d = collections.defaultdict(set)
        for i in range(n):
            d[arr[i]].add(i)
        curs, other = set([0]), set([n-1])  # store layers from start and layers from end
        visited = {0, n-1}
        step = 0
​
        while curs: # when current layer exists
            if len(curs) > len(other): # search from the side with fewer nodes
                curs, other = other, curs
            nex = set()
            for node in curs: # iterate the layer
                for child in d[arr[node]]: # check same value
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)
                d[arr[node]].clear() # clear the list to prevent redundant search
                for child in [node-1, node+1]: # check neighbors
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)
            curs = nex
            step += 1
        
#         #soln 0 - Jake's solution BFS
#         d = collections.defaultdict(set)
#         for i in range(len(arr)-1,-1,-1):
#             d[arr[i]].add(i)
        
#         end = len(arr) - 1
#         queue = collections.deque([(0,0)])
#         seen = set([0])
#         d[arr[0]].remove(0)
        
#         while queue:
#             cur,depth = queue.popleft()
#             if cur == end: return depth
#             if arr[cur] in d:
#                 for j in d[arr[cur]]:
#                     if j not in seen:
#                         queue.append((j,depth+1))
#                         seen.add(j)
#                 del d[arr[cur]]
#             for j in [cur - 1, cur + 1]:
#                 if 0 <= j <= end and j not in seen:
#                     queue.append((j,depth+1))
#                     seen.add(j)
