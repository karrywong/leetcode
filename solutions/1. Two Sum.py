class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lib = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp not in lib:
                lib[num] = i 
            else:
                return [lib[temp], i]
            
