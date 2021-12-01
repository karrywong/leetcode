class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #Totally stuck, tried with stack a few times
        #Leetcode linear scan, really clever
        first_num, second_num = float('inf'), float('inf')
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False
