class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [i for i in range(n) if nums[i] % 2 == 1]
        if len(odd) < k: return 0
        if len(odd) == k: return (odd[0] + 1) * (n - odd[-1])
        
        # len(odd) > k 
        i, j = 0, k-1
        res = 0
        
        while j < len(odd):
            if i == 0:
                res += (odd[i] + 1) * (odd[j+1] - odd[j])
                
            elif j == len(odd) - 1:
                res +=  (odd[i] - odd[i-1]) * (n - odd[j])
                
            else:
                res += (odd[i] - odd[i-1]) * (odd[j+1] - odd[j])
​
            i += 1
            j += 1
            
        return res
    
#ex1 odd = [0,1,3,4], k = 3
# i=0, j=2 -> res += (0 + 1) * (4 - 3) = 1
# i=1, j=3 -> res += (1 - 0) * (5 - 4) = 1
​
#ex2 odd = [], k = 1
# return 0
​
#ex3, odd = [3,6], k = 2
# return (3+1)*(10 - 6) = 16
​
#Input: nums = [2,2,2,1,2,2,1,2,2,2,1,2,2], k = 2
#ex4 odd = [3,6,10], k = 2
# i=0, j=1, res += (3+1) * (10 - 6) = 16
# i=1, j=2, res += (6-3) * (13 - 10) = 6
# return 22
​
​
