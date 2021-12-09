class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        #First attempt, sort array according to distance to parabola verterx
        n = len(nums)
        if a != 0:
            nums.sort(key = lambda x : abs(x+0.5*b/a))
        else:
            nums.sort()
        f = lambda x : a*x*x+b*x+c
        left, right = 0, n-1
        ans = [0] * n
        for i in range(n-1, -1, -1):
            lval = f(nums[left])
            rval = f(nums[right])
            if lval < rval:
                ans[i] = rval
                right -= 1
            else:
                ans[i] = lval
                left += 1
        return ans
