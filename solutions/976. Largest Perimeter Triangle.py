class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #Time O(NlogN), space O(1)
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            a, b, c = nums[i:i+3]
            if b+c>a: #a+b>c and a+c>b and - not necessary
                return a+b+c
        return 0
