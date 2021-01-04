class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = set(nums)
        answer = nums[0]
        temp1 = 0
        for e in elements:
            temp2 = nums.count(e)
            if temp1 < temp2:
                answer = e
                temp1 = temp2
        return answer
        
