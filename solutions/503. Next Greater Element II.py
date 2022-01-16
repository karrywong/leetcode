class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #First attempt, time O(N), space O(N)
        n = len(nums)
        ans = [-1]*n
        htb = {}
        stack = []
        
        for i, num in enumerate(nums+nums[:-1]):
            while stack and num > nums[stack[-1]%n]:
                ans[stack.pop()%n] = num
            stack.append(i)
        return ans
