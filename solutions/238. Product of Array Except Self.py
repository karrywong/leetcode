class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         temp1 = 1
#         lst1 = []
#         for n in nums[:len(nums)-1]:
#             temp1 = temp1 * n
#             lst1.append(temp1) 
#         #lst1 = [1,2,6]
            
#         temp2 = 1
#         lst2 = []
#         for i in range(len(nums)-1, 0, -1):
#             temp2 = temp2 * nums[i]
#             lst2.append(temp2)
#         #lst2 = [4,12,24] -> [12,4]
        
#         res = []
#         res.append(lst2[-1])
#         lst2.pop(-1)
#         lst2 = lst2[::-1]
#         for i in range(0, len(nums)-2):
#             res.append(lst1[i] * lst2[i])
#         res.append(lst1[-1])
        
#         return res
​
    
        ### Soln - solution suggested by Haotian Li, left & right products
        n = len(nums)
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
