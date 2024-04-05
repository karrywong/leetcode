class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n, ans = len(nums), []
        total = 2*k+1
        if k == 0: return nums
        for i in range(n):
            if i < k or i > n-1-k:
                ans.append(-1)
            elif i == k:
                sw = sum(nums[:total]) #sliding window
                ans.append(sw//total)
            else: # k+1 <= i <= n-1-k
                sw -= nums[i-k-1]
                sw += nums[i+k]
                ans.append(sw//total)
        return ans
                            
