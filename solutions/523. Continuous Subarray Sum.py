class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # soln by ZitaoWang, time O(N), space O(N)
        cur_sum = 0
        lib = {0:-1}
        for i, num in enumerate(nums):
            cur_sum = (cur_sum + num) % k
            if cur_sum in lib:
                if i - lib[cur_sum] > 1:
                    return True
            else:
                lib[cur_sum] = i
        return False
