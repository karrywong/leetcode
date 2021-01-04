class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lib = {}
        for i in range(0, len(nums)):
            temp = target - nums[i]
            if temp not in lib:
                lib[nums[i]] = i 
            else:
                return [lib[temp], i]
            
