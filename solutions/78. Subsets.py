class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[], [nums[0]]]
        if len(nums) == 1: return res
        
        for i in range(1, len(nums)):
            temp = [[] for x in range(len(res))]
            for j in range(0, len(res)):
                temp[j] = res[j] + [nums[i]]
            res = res + temp
  
        return res
