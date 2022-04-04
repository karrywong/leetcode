        elif root.val > key:
            root.left = self.insert(root.left, key)
        else:
            root.cnt += 1
            root.right = self.insert(root.right, key)
        
        return root
    
    def findKthLargest(self, root, k):
        if not root: return -1
        
        elif root.cnt == k: return root.val
        
        elif root.cnt > k:
            return self.findKthLargest(root.right, k)
        else:
            return self.findKthLargest(root.left, k - root.cnt -1)
    
#     def __init__(self, k: int, nums: List[int]):        
#         #Leetcode, much cleaner
#         self.k = k 
#         self.heap = nums
#         heapq.heapify(self.heap)
#         while len(self.heap) > k:
#             heapq.heappop(self.heap)
        
#     def add(self, val: int) -> int:
#         heapq.heappush(self.heap, val)
#         if len(self.heap) > self.k:
#             heapq.heappop(self.heap)
#         # print(self.heap)
#         return self.heap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
