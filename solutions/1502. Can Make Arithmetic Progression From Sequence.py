class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        #Time O(N), space O(N), by lenchen1112 - check if all numbers are evenly distributed.
        m = min(arr)
        gap = (max(arr) - m) / (len(arr) - 1)
        if gap == 0: 
            return True
        s = set(num - m for num in arr)
        return len(s) == len(arr) and all(diff % gap == 0 for diff in s)
        
        # #Time O(NlogN), space O(1), straightforward count
        # arr.sort()
        # val = arr[1] - arr[0]
        # for i in range(1,len(arr)-1):
        #     if arr[i] + val != arr[i+1]:
        #         return False
        # return True
