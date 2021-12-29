class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
#         #DP solution, tables for subarray w pos & neg products, time O(N), space O(N)
#         n = len(nums)
#         pos, neg = [0]*n, [0]*n
#         if nums[0] > 0: 
#             pos[0] = 1
#         elif nums[0] < 0:
#             neg[0] = 1
        
#         for i, num in enumerate(nums[1:],1):
#             if num > 0:
#                 pos[i] = pos[i-1] + 1 #positive = previous positive * positive number
#                 if neg[i-1]:
#                     neg[i] = neg[i-1] + 1 #negative = previous negative * positive number
#             elif num < 0:
#                 neg[i] = pos[i-1] + 1 #negative = previous positive * negative number
#                 if neg[i-1]:
#                     pos[i] = neg[i-1] + 1 #postive = previous negative * negative number
#         return max(pos)
​
        #Following hints, soln by donoewth
        sub = [] # sub: non zero sub-array derived from nums (use 0 as split point)
        s = [] # generate subarray
        for i, n in enumerate(nums):
            if n != 0:
                s.append(n)
            if n == 0:
                sub.append(s)
                s = []
        sub.append(s)
        
        # get the maximum length of positive product for each sub array 
        # I: if all positive, then we collect all elements
        # II: if negative numbers are even, we also collect all elements
        # III: if negative numbers are odd, we skip the first or the last of the number to find the maximum length
        def max_leng(arr):
            return len(arr) if all_positive(arr) or even_neg(arr) else max(pick_left(arr), pick_right(arr))
        
        def all_positive(arr): # return true if all the elements are above 0
            for a in arr:
                if a < 0:
                    return False
            return True
        
        def even_neg(arr): # return true if the number of neg numbers are even
            c = 0
            for a in arr:
                if a < 0:
                    c += 1
            return c % 2 == 0
        
        def pick_left(arr): # skip the first negative number, return the remaining length
            for i, a in enumerate(arr):
                if a < 0:
                    return len(arr) - i - 1
        
        def pick_right(arr): # skip the last negative number, return the remaining length
            arr.reverse()
            for i, a in enumerate(arr):
                if a < 0:
                    return len(arr) - i - 1
        opt = []
        for s in sub: # iterate all the sub-array to find the max length
            opt.append(max_leng(s))
        return max(opt) # return the max value 
