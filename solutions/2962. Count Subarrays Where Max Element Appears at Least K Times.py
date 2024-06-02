class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # [1,3,2,3,3,0], k=2 -> 6+4=10
        # end=5, start=4
        # ans = 2+4+4=10
        
        # [1,3,2,3,0], k=2  
        # end=4, start=2
        # ans = 2+2=4
    
        # leetcode idea I - sliding window, time O(N), space O(1)
        left_ptr = 0
        count = 0
        max_ele = max(nums)
        ans = 0
        
        for right_ptr in range(len(nums)):
            if nums[right_ptr] == max_ele:
                count += 1
                
            while count == k:
                if nums[left_ptr] == max_ele:
                    count -= 1
                left_ptr += 1
            ans += left_ptr
        return ans
    
#         # leetcode idea II - frequency + indices, time O(N), space O(N)
#         max_ele = max(nums)
#         indices = []
#         ans = 0
        
#         for idx, num in enumerate(nums):
#             if num == max_ele:
#                 indices.append(idx)
                
#             if len(indices) >= k:
#                 ans += indices[-k] + 1
#         return ans
​
