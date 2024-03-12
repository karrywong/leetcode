import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    # start time: 7:40pm
    # len(nums) > 0
    # k <= len(nums)
    # num in nums (+) or (-) 
    
    # max heap, time O(Nlogk), space O(k)
        hp = []
        heapq.heapify(hp)
        for num in nums: #num = 6
            if len(hp) >= k:
                heapq.heappushpop(hp, num) 
            else:
                heapq.heappush(hp, num)
        return hp[0]
​
    # # time O(N), space O(len(cnt) = (max_val - min_val) / step_size)
    # # cnt = [1, .., 3, 4, 1] #O(N)
    # cul_sum = 0
    # for i in range(len(cnt)-1,-1,-1):
    #     cul_sum += cnt[i]
    #     if cul_sum >= k:
    #         return i
    # return 
​
    # #Sorting, time O(NlogN), space O(1)
    # nums.sort()
    # return nums[-k]
​
    #Heap, time O(NlogK), Space O(k)
    # return heapq.nlargest(k, nums)[-1]
    
    # num = [499, 1, 5, 40,....] 
    
    # nums = [3,2,3,1,2,4,5,5,6], k = 4
    # hp = [4,5,5,6]
    # <- decreasing order
    # return 4
    
    
#     #LeetCode's quickselect, time O(N^2), space O(N)
#     def partition(left, right, pivot_index) -> int:
#         pivot = nums[pivot_index]
#         nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
​
#         store_index = left
#         for i in range(left, right):
