class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Second attempt w sliding window, time O(N), space O(N)
        #Inspired by b0mb4rdi3r in discussion
        seen = set()
        i = 0
        for j in range(len(nums)):
            if j-i>k:
                seen.remove(nums[i])
                i += 1
                
            if nums[j] in seen:
                return True
            else:
                seen.add(nums[j])
        return False
    
        # #First attempt w dictionary, time O(N), space O(N)
        # htb = {}
        # for i, num in enumerate(nums):
        #     if num in htb and i - htb[num] <= k:
        #         return True
        #     else:
        #         htb[num] = i
        # return False
