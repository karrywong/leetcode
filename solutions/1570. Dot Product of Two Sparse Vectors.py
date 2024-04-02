class SparseVector:
    def __init__(self, nums: List[int]):
        self.lst = [(idx, num) for idx, num in enumerate(nums) if num > 0]
        
    # Return the dotProduct of two sparse vectors
    # time O(L1+L2), space O(L1+L2), w/ L1, L2 = # nonzero elements in vec1, vec2
    def dotProduct(self, vec: 'SparseVector') -> int:
        i, j = 0, 0
        n, m = len(self.lst), len(vec.lst)
        ans = 0
        while i < n and j < m:
            if self.lst[i][0] == vec.lst[j][0]:
                ans += self.lst[i][1] * vec.lst[j][1]
                i += 1
                j += 1
            elif self.lst[i][0] < vec.lst[j][0]:
                i += 1
            else:
                j += 1
        return ans
        
​
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
