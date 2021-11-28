class Solution:
    #First attempt, directly use random.randint to generate permutations
    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.nums_perm = nums[:]
        self.n = len(nums)
        
    def reset(self) -> List[int]:
        return self.nums
​
    def shuffle(self) -> List[int]:
        i = random.randint(0, self.n-1)
        j = random.randint(0, self.n-1)
        self.nums_perm[i], self.nums_perm[j] = self.nums_perm[j], self.nums_perm[i]
        return self.nums_perm
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
