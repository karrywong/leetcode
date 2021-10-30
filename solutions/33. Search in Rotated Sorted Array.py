class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # soln - LeetCode one-pass binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[mid] > target and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: #nums[mid] < nums[l]
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # print(l,r, mid)
        return -1
        
