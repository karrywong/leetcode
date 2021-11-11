class Solution:
    def jump(self, nums: List[int]) -> int:
        #soln 1 - Leetcode greedy
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps
        
#         # BFS, Jake's solution
#         end = len(nums) - 1
#         if end == 0: return 0
        
#         queue = collections.deque([(0,0)]) # (index,depth)
#         seen = set([0])
#         while queue:
#             cur_ind,depth = queue.popleft()
#             for i in range(nums[cur_ind],0,-1):
#                 next_ind = cur_ind + i
#                 if next_ind >= end:
#                     return depth + 1
#                 if next_ind not in seen:
#                     queue.append((next_ind,depth+1))
#                     seen.add(next_ind)
