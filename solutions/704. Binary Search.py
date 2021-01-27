class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        ### Soln - method of bisection O(log(N))
        l, r = 0, len(nums) - 1
        
        while (l <= r):
            if target < nums[l] or target > nums[r]: 
                break
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else: 
                r = mid - 1
        
        return -1
​
        ### Soln - cheating with built-in function
        # try:
        #     return nums.index(target)
        # except:
        #     return -1
