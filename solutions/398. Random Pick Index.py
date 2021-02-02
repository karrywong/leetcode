class Solution:
​
    def __init__(self, nums: List[int]):
        # self.nums = nums
        self.lib = collections.defaultdict(list)
        
        for i, n in enumerate(nums):
            self.lib[n].append(i)
        
    def pick(self, target: int) -> int:
        # lst = [i for i, x in enumerate(self.nums) if x == target]
        return random.choice(self.lib[target])
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
​
