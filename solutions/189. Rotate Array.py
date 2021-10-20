class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #soln 2 - cyclic replacements
        n = len(nums)
        k %= n
        start, count = 0, 0
        while count < n:
            cur, prev = start, nums[start]
            while True:
                next_id = (cur+k)%n
                nums[next_id], prev = prev, nums[next_id]
                cur = next_id
                count += 1
                if start == cur: break
            start += 1
            
        # #soln 1 - reversal time O(n), space O(1)
        # nums.reverse()
        # k %= len(nums)
        # nums[:k] = nums[:k][::-1]
        # nums[k:] = nums[k::][::-1]
        
        # #soln 0 - violation of the in-place rule
        # for i in range(k):
        #     nums.insert(0, nums.pop())
