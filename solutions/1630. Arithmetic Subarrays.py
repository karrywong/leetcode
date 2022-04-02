class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        #Second attempt, use set w/o sorting, time O(N*M)
        def isArith(arr: List[int]) -> bool:
            arr_set = set(arr)
            if len(arr_set) != len(arr):
                return len(arr_set) == 1
            maxval, minval = max(arr), min(arr)
            step = (maxval-minval) / (len(arr)-1)
            val = minval
            for i in range(len(arr)-1):
                val += step
                if val not in arr_set:
                    return False
            return True
        return [isArith(nums[start: end+1]) for start, end in zip(l,r)]
        
        #First attempt, following the hints, time O(N * MlogM), space O(M), where N = len(l), M = len(nums)
        # def isArith(arr: List[int]) -> bool:
        #     if len(arr) == 1: return True
        #     arr.sort()
        #     val = (arr[-1] - arr[0]) / (len(arr)-1)
        #     return all(arr[i+1]-arr[i] == val for i in range(len(arr)-1))
        # return [isArith(nums[start: end+1]) for start, end in zip(l,r)]
