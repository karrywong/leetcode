class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #Soln 2 - Leetcode, Time O(N), find max three and min two values
        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for n in nums:
            if n <= min1:
                min2, min1 = min1, n
            elif n <= min2:
                min2 = n
            if n >= max3:
                max3, max2, max1 = n, max3, max2
            elif n >= max2:
                max2, max1 = n, max2
            elif n >= max1:
                max1 = n 
        return max(max3*max2*max1, min1*min2*max3)
        
        ### Soln 1 - sorting, Time O(NlogN), Space O(N)
        nums.sort()
        return max( nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1] )
        
​
        
