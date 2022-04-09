#BIT soln, inspired by hiepit <https://leetcode.com/problems/range-sum-query-mutable/discuss/1406686/C%2B%2BJavaPython-Binary-Indexed-Tree>
#Refer to Fenwick tree <https://en.wikipedia.org/wiki/Fenwick_tree> 
class BIT:
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (size + 1)
    
    def getSum(self, idx):  # Get sum in range [1..idx], 1-based indexing
        val = 0
        while idx > 0:
            val += self.bit[idx]
            idx -= idx & (-idx)
        return val
        
    def getSumRange(self, left, right):  # left, right inclusive, 1-based indexing
        return self.getSum(right) - self.getSum(left)
        
    def addValue(self, idx, val):  # 1-based indexing
        while idx <= self.size:
            self.bit[idx] += val
            idx += idx & (-idx)
            
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BIT(len(nums))
        for i, v in enumerate(nums):
            self.bit.addValue(i+1, v)
        # print(self.bit.bit)
        
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.bit.addValue(index+1, diff)
        self.nums[index] = val
​
    def sumRange(self, left: int, right: int) -> int:
        return self.bit.getSumRange(left, right+1)
​
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
