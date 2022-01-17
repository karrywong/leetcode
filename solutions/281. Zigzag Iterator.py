class ZigzagIterator:
    #LeetCode queue of pointers, time O(1), space O(K)
    def __init__(self, v1: List[int], v2: List[int]):
        self.vec = [v1,v2]
        self.queue = collections.deque()
        for index, vector in enumerate(self.vec):
            if len(vector) > 0:
                self.queue.append((index,0))
    def next(self) -> int:
        if self.queue:
            vec_ind, elem_ind = self.queue.popleft()
            next_elem_ind = elem_ind + 1
            if next_elem_ind < len(self.vec[vec_ind]):
                self.queue.append((vec_ind, next_elem_ind))
            return self.vec[vec_ind][elem_ind]
            
    def hasNext(self) -> bool:
        return len(self.queue) > 0
        
#     #LeetCode two pointers, time O(K), space O(1)
#     def __init__(self, v1: List[int], v2: List[int]):
#         self.vec = [v1,v2]
#         self.p_elem = 0 #ptr to index of element
#         self.p_vec = 0 #ptr to vec
#         self.total_num = len(v1) + len(v2)
#         self.output_count = 0
#     def next(self) -> int:
#         iter_num = 0
#         ans = None
#         while iter_num < len(self.vec):
#             curr_vec = self.vec[self.p_vec]
#             if self.p_elem < len(curr_vec):
#                 ans = curr_vec[self.p_elem]
#             iter_num += 1
#             self.p_vec = (self.p_vec+1) % len(self.vec)
            
#             if self.p_vec == 0:
#                 self.p_elem += 1
#             if ans is not None:
#                 self.output_count += 1
#                 return ans
        
#     def hasNext(self) -> bool:
#         return self.output_count < self.total_num
    
#     #First attempt, time O(1), space O(M+N)
#     def __init__(self, v1: List[int], v2: List[int]):
#         m, n = len(v1), len(v2)
#         self.queue = collections.deque()
#         for a,b in zip(v1,v2):
#             self.queue.append(a)
#             self.queue.append(b)
#         if m > n:
#             self.queue += v1[n:] 
#         elif m < n:
#             self.queue += v2[m:] 
#     def next(self) -> int:
#         return self.queue.popleft()
#     def hasNext(self) -> bool:
#         return True if self.queue else False        
​
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
