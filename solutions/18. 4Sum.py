class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #soln 0 - first attempt, two pointers, Time O(N^3), Space O(N)
        #Similar to 15. 3Sum
        def twoSum(i, j, target3, ans):
            l, r = j+1, len(nums)-1
            while l < r:
                val = nums[l] + nums[r]
                if val < target3:
                    l += 1
                elif val > target3:
                    r -= 1
                else:
                    ans.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        def threeSum(i, target2, ans):
            for j in range(i+1,len(nums)-2):
                if j == i+1 or nums[j] != nums[j-1]:
                    target3 = target2 - nums[j]
                    twoSum(i, j, target3, ans)
        
        ans = []
        nums.sort()
        print(nums)
        for i in range(len(nums)-3):
            target2 = target - nums[i]
            if i == 0 or nums[i] != nums[i-1]:
                threeSum(i, target2, ans)
        return ans
