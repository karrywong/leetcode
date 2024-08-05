class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # soln 2 - cyclic replacements
        # Time O(N), Space O(1)
        start, count = 0, 0
        k %= len(nums)
        
        while count < len(nums):
            cur, prev  = start, nums[start]
            while True:
                next_idx = (cur+k) % len(nums)
                nums[next_idx], prev = prev, nums[next_idx]
                cur = next_idx
                count += 1
                if start == cur:
                    break
            start += 1
        return
        
        # # #soln 1 - reversal time O(n), space O(1)
        # nums.reverse()
        # k %= len(nums)
        # nums[:k] = nums[:k][::-1]
        # nums[k:] = nums[k::][::-1]
        
        # #soln 0 - violation of the in-place rule
        #Time O(N * k), Space O(1)
        # for i in range(k):
        #     nums.insert(0, nums.pop())
