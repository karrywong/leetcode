class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ### Soln 1 - brute force
        # answer = [-1]*len(nums)
        # for i, n in enumerate(nums):
        #     for m in nums[i+1:] + nums[0:i]:
        #         if m > n:
        #             answer[i] = m
        #             break
        # return answer
        
        ### Soln 2 - stack (reversed scan twice)
        l = len(nums)
        nums_temp = nums[::-1]*2
        stack = []
        answer = [-1]*len(nums)
        
        for i in range(0, len(nums_temp)):
            while stack:
                if nums_temp[i] >= stack[-1]:
                    stack.pop()
                else:
                    answer[i % l] = stack[-1]
                    break
            stack.append(nums_temp[i])
                        
        return answer[::-1]
​
        
        ###Soln 3 - stack (forward scan twice, clever! from jasperjoe in discussion):
        # stack=[]
        # res=[-1 for i in range(len(nums))]
        # tem=nums[:]+nums[:]
        # for i in range(len(tem)):
        #     while stack and tem[i]>tem[stack[-1]]:
        #         res[stack.pop()]=tem[i]
        #     if i<len(nums):
        #         stack.append(i)
        # return res
