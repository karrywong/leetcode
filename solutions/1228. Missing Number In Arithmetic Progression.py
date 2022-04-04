class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        #Time O(N), space O(1)
        step = (arr[-1] - arr[0]) // len(arr)
        if step == 0: return arr[0]
        val = arr[0]
        for i in range(len(arr)-1):
            val += step
            if val != arr[i+1]:
                return val
