from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        #Mock interview, only figured out the optimal O(N*logN) soln after 60 min with no coding...
#         tasks = [10,15,30]
#         workers = [1,2,5,15,20] -> 
#         pills = 3, strength = 10
        
#         worker 0 (1+10) -> 10
#         worker 1 (2+10) -> continue 
#         worker 2 (5+10) -> 15
#         worker 3 -> continue
        
#         task = [10,20]
#         workers = [9,15,15] -> [15,15]
#         pills = 1, strength = 5
#         #Karry -> 1 task
#         #Cho -> 2 task
        
#         #N+(N-1) +... + 1 = N^2 -> NlogN -> N
#         task = [9,10] #(N)
#         worker = [5,6] #(N)
#         pill = 2, strength = 5
        
        #binary search in [0, K=min(len(tasks), len(workers))], time O(N*(logN)^2), space O(K)
#         def isPossible(k: int, p: int) -> bool: #Failed
#             t_arr = tasks[:k]
#             w_arr = workers[-k:]
#             # print(k, p, t_arr, w_arr)
#             if t_arr[-1] <= w_arr[0]:
#                 return True
            
#             ptr = -1
#             w_ind = 0
#             while w_ind < k and p > 0:
#                 w_arr[w_ind] += strength
#                 while ptr+1 < len(t_arr) and t_arr[ptr+1] <= w_arr[w_ind]:
#                     ptr += 1
#                 if ptr == -1: 
#                     return False
#                 t_arr.pop(ptr)
#                 ptr -= 1
#                 p -= 1
#                 w_ind += 1 
            
#             if w_ind == k:
#                 return True
#             elif p > 0:
#                 for i in range(w_ind, min(w_ind+p+1,k)):
#                     w_arr[i] += strength
            
#             return all(w >= t for w, t in zip(w_arr[w_ind:], t_arr))
        
        def isPossible(k):
            wList = workers[-k:]
            tries = pills
​
            for t in tasks[:k][::-1]:
                idx = bisect.bisect_left(wList, t)
                if idx < len(wList):
                    wList.pop(idx)
                elif tries > 0:
                    idx = bisect.bisect_left(wList,t-strength)
                    if idx < len(wList):
                        wList.pop(idx)
                        tries -= 1
                else:
                    return False
            return len(wList) == 0
    
        tasks.sort()
        workers.sort()
        l, r = 0, min(len(tasks), len(workers))+1
        while l+1 < r:
            mid = l + (r-l)//2
            # print(l,r,mid)
            if isPossible(mid):
                l = mid
            else:
                r = mid
        return l
