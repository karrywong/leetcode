class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # ## Soln 1 - two pointer
        # pointer = 0
        # for i, n in enumerate(nums):
        #     if n != val:
        #         nums[pointer] = nums[i]
        #         pointer += 1
        # return pointer
    
        # Soln 1 - two pointer, optimal
        i = 0
        temp_length = len(nums)
        while i < temp_length:
            if nums[i] == val:
                nums[i] = nums[temp_length-1];
                temp_length -= 1
            else:
                i += 1
        return temp_length
