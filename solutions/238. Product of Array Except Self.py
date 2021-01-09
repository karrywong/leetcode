#         lst2 = lst2[::-1]
#         for i in range(0, len(nums)-2):
#             res.append(lst1[i] * lst2[i])
#         res.append(lst1[-1])
        
#         return res
​
​
        # ### Soln - clever from discussion by ZitaoWang
        # res = [1]*len(nums)
        # lprod = 1
        # rprod = 1
        # for i in range(len(nums)):
        #     res[i] *= lprod
        #     lprod *= nums[i]
        #     res[~i] *= rprod
        #     rprod *= nums[~i]
        #     # print(i, ~i, res, lprod, rprod)
        # return res
        
        
        ### Soln - solution by Haotian Li, second for-loop faster
        n = len(nums)
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            right[n-i -1] = right[n-i] * nums[n-i]
        
        return [left[i]*right[i] for i in range(n)]
        
