class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # #soln 2 - heapsort using built-in heapq
        # heapq.heapify(nums)
        # return [heapq.heappop(nums) for i in range(len(nums))]
        
        #soln 1 - mergesort by dlwsdqdws, Time O(NlogN)
        if len(nums) <= 1:
            return nums
        middle = len(nums) // 2
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])
        merged = []
        while left and right:
            if left[0] <= right [0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(right if right else left)
        return merged
