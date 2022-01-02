class Solution:
    def countArrangement(self, n: int) -> int:
        #Leetcode better brute force
        self.ans = 0
        nums = [i for i in range(1,n+1)]
        def permute(nums, l):
            if l == len(nums):
                self.ans += 1
        
            for i in range(l,len(nums)):
                nums[i], nums[l] = nums[l], nums[i]
                if (nums[l] % (l+1) == 0 or (l+1) % nums[l] == 0):
                    permute(nums, l+1)
                nums[i], nums[l] = nums[l], nums[i]
        
        permute(nums,0)
        return self.ans
            
#         # [, , ,4] -> ans = 3 in n=3 (base case)
#         # [1,2,3] all permutations 3! = 6
#         # [, ,4, ], [,4, , ], [4, , ,] 
#         # [, ,4, ] impossible, 
#         # [,4, , ] -> [1,4,3,2], [3,4,1,2], [2,4,3,1]
#         # [4, , ,] -> [4,2,3,1], [4,1,3,2]
#         # ans += 4 -> ans = 10
        
#         #Mock interview practice, up to n =12, Memory limit exceeded 
#         htb = {1:1}
#         def helper(n):
#             if n in htb:
#                 return htb[n]
            
#             ans = helper(n-1)
#             possible_perm = list(itertools.permutations([i for i in range(1,n)]))
            
#             for i in range(n-1): #n > i+1
#                 if n % (i+1) == 0: 
#                     lst = [j for j in range(1,i+1)] + [j for j in range(i+2,n+1)]
#                     # print(n,i+1, lst,[p for p in possible_perm])
#                     for perm in possible_perm:
#                         for l,p in zip(lst, perm):
