class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #  nums = [0,2,1,5,3,4], len = 6
        
        # nums = [5,0,1,2,3,4], len = 6
        # nums = [4*6+5,5*6+0,0*6+1, 1*6+2,2*6+3, 3*6+4]
        # nums = [4,5,0,1,2,3]
        # r = nums[i], b = nums[nums[i]] % q, nums[i] = q*b+r
        
        
        # # time O(N), space O(N)
        # ans=[]
        # for i in range(len(nums)):
        #     ans.append(nums[nums[i]])
        # return ans
    
        # time O(N), space O(1)
        q = len(nums)
        for i in range(q):
            nums[i] += q*(nums[nums[i]] % q)
        
        for i in range(q):
            nums[i] //=q
        return nums
        
