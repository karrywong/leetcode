class Vector2D:
    #Leetcode two pointers, cleaner
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.inner = 0
        self.outer = 0
        
    def advance_to_next(self):
        while self.outer < len(self.vec) and self.inner == len(self.vec[self.outer]):
            self.outer += 1
            self.inner = 0
​
    def next(self) -> int:
        self.advance_to_next()
        ans = self.vec[self.outer][self.inner]
        self.inner += 1
        return ans
​
    def hasNext(self) -> bool:
        self.advance_to_next()
        return self.outer < len(self.vec)
    
#     #Two pointers, almost identical to 281. Zigzag Iterator, time O(N+V)/N = O(V/N), space O(1)
#     def __init__(self, vec: List[List[int]]):
#         self.vec = vec
#         self.p_elem = 0 #ptr to index of element
#         self.p_vec = 0 #ptr to vec
#         self.total_num = 0
#         for i in range(len(vec)):
#             self.total_num += len(vec[i])
#         self.output_count = 0        
​
#     def next(self) -> int:
#         iter_num = 0
#         curr_vec = self.vec[self.p_vec]
#         ans = None
#         if ans is None:
#             while self.p_elem == len(curr_vec):
#                 self.p_vec += 1
#                 curr_vec = self.vec[self.p_vec]
#                 self.p_elem = 0
#             ans = curr_vec[self.p_elem]
#             self.p_elem += 1
​
#         self.output_count += 1
#         return ans
​
#     def hasNext(self) -> bool:
#         return self.output_count < self.total_num
​
# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
