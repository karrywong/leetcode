class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # time O(N), space O(1)
        left_ptr=0
        prev = -1
        ans = 0
        for right_ptr in range(len(nums)):
            num = nums[right_ptr]
            if num == prev:
                left_ptr = right_ptr
            ans += right_ptr-left_ptr+1
            prev = num
            
        return ans
        
        # Testing
        # [0,1,1,1]
        #        l
        #        r
        
        # num = 1, prev = 1
        # ans = 1+2+1+1 = 5
        
        # [0,1,1,0]
        # ans = 1+2+1+2 = 6
        
