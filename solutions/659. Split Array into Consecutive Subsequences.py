class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        #Monotonic increasing queue, (start_digit)
        #eg1, counter = {2:1, 3:2, 4:1, 5:1}, queue = [3]
        #eg2, [1,2,3,3,4,4,5,5], counter = {1:1, 2:1, 3:2, 4:2, 5:2}, queue = [1,3]
        #eg3, [1,2,3,4,4,5,6], counter = {1:1, 2:1, 3:1, 4:2, 5:1, 6: 1, 7:0}, queue = [4]
        #[1,2,3,4], counter = {1:1, 2:1, 3:1, 4:1}, queue = [1]
        
        #Time O(N), space O(N)
        counter = collections.Counter(nums) #O(N)
        counter[nums[-1]+1] = 0
        queue = collections.deque()
        last = nums[0]-1
        
        for k in range(nums[0], nums[-1]+2):             
            if k - last > 1: 
                return False
            if counter[k] > len(queue):
                queue.extend([k] * (counter[k]-len(queue)))
            elif counter[k] < len(queue):
                excess = len(queue) - counter[k]
                while excess:
                    if k-queue[0] >= 3:
                        queue.popleft()
                        excess -= 1
                    else:
                        return False
            last = k
        return True
    
#         #First attempt, heap time O(N*NlogN), TLE
#         hp = [(1, nums[0])]
#         heapq.heapify(hp)
#         for num in nums[1:]:
#             stack = []
#             found = False
#             while hp:
#                 if num-hp[0][1] == 1:
#                     length, last_digit = heapq.heappop(hp)
#                     heapq.heappush(hp, (length+1, num))
#                     found = True
#                     break
#                 stack.append(heapq.heappop(hp))
​
#             if not found:
#                 heapq.heappush(hp, (1, num))
#             while stack:
#                 heapq.heappush(hp, stack.pop())
        
#         return hp[0][0] >= 3
