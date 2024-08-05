class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # time O(N), space O(1)
        ptr = len(nums)-1
        for idx in range(len(nums)-1, -1, -1):
            if nums[idx] == val:
                nums[idx], nums[ptr] = nums[ptr], nums[idx]
                ptr -= 1
        return ptr+1
​
        # #Recent attempt - reverse order
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] == val:
        #         nums.pop(i)
        # return len(nums)
        
        ### Soln 1 - two pointer
        # pointer = 0
        # for i, n in enumerate(nums):
        #     if n != val:
        #         nums[pointer] = nums[i]
        #         pointer += 1
        # return pointer
​
        # # Soln 3 - oneliner, clever idea from discussion
        # while val in nums: nums.remove(val)
