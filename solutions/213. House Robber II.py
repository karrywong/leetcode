class Solution:
    def rob(self, nums: List[int]) -> int:
        ### Reduce the given problem into two original problems of House Robber
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums)
        elif len(nums) == 3: return max(nums)
        
        lst1 = nums[1:]
        lst2 = nums[:-1]
        
        lst1[2] += lst1[0]
        for i in range(3, len(lst1)):
            lst1[i] += max(lst1[i-2], lst1[i-3])
            
        lst2[2] += lst2[0]
        for i in range(3, len(lst2)):
            lst2[i] += max(lst2[i-2], lst2[i-3])
            
        return max(max(lst1), max(lst2))
