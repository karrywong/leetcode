class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        #Leetcode DFS w negative marking
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            arr[start] = -arr[start]
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
        return False
        
        # #Leetcode BFS w negative marking
        # n = len(arr)
        # q = [start]
        # while q:
        #     node = q.pop(0)
        #     if arr[node] == 0: #check if reach zero
        #         return True
        #     if arr[node] < 0:
        #         continue
        #     for i in [node + arr[node], node - arr[node]]:
        #         if 0 <= i < n:
        #             q.append(i)
        #     arr[node] = -arr[node] #negative marking
        # return False
        
#         # BFS - first attempt
#         if arr[start] == 0: return True
#         end = len(arr) - 1
        
#         queue = collections.deque([start]) #start index
#         seen = set([start])
#         while queue:
#             cur_ind = queue.popleft()
#             step = arr[cur_ind]
#             left_ind = cur_ind - step
#             if left_ind >= 0:
#                 if arr[left_ind] == 0:
#                     return True
#                 if left_ind not in seen:
#                     queue.append(left_ind)
#                     seen.add(left_ind)
                    
#             right_ind = cur_ind + step
#             if right_ind <= end:
#                 if arr[right_ind] == 0:
#                     return True
#                 if right_ind not in seen:
#                     queue.append(right_ind)
#                     seen.add(right_ind)
#         return False
