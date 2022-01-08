class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         #Time O(N^2), Space O(N)
#         htb = {-1:0} #key = index, value = culmulative sum
#         ans = 0
#         cur_sum = 0
#         for i in range(len(arr)):
#             ans += arr[i]
#             cur_sum += arr[i]
#             htb[i] = cur_sum
            
#             count = 1 
#             while i-2*count-1 >= -1:
#                 ans += htb[i] - htb[i-2*count-1]
#                 count += 1
#         return ans
        
        #count how many times will arr[k] appear in the total sum  
        #Time O(N), space O(1), by yaok09
        res = 0
        for i in range(len(arr)):
            res += ((i + 1) * (len(arr) - i) + 1) // 2 * arr[i]
        return res
        
        #[1,4,2,5,3]
        #cur_sum = [1,5,7,12,15]
        
        #i = 2, ans = 1 + 4 + (7-0)
        #i = 3, ans += 5 + (12-1)
        #i = 4, ans += 3 + (15-5) + (15-0)
