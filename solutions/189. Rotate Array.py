class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #soln 1 - reversal
        nums.reverse()
        k %= len(nums)
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k::][::-1]
        
        # #soln 0 - violation of the in-place rule
        # for i in range(k):
        #     nums.insert(0, nums.pop())
