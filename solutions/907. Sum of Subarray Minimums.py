class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # #brute force, time O(N^2), space O(1)
        # ans = 0
        # for i in range(len(arr)):
        #     mi = arr[i]
        #     ans += arr[i]
        #     for j in range(i+1, len(arr)):
        #         mi = min(mi, arr[j])
        #         ans += mi
        # return ans % (10**9+7)
    
        #Almost identical to 2104. Sum of Subarray Ranges
        #Time O(N), space O(N)
        ans = 0
        stack = [] #(I)
        arr1 = [float('-inf')]+arr+[float('-inf')]
        for i, val in enumerate(arr1):
            while stack and arr1[stack[-1]] > val:
                j = stack.pop()
                k = stack[-1]
                ans += arr1[j]*(i-j)*(j-k)
            stack.append(i)
        return ans % (10**9+7)
