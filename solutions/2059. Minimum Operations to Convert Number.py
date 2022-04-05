class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        #BFS, time O(range), space O(range)
        #if start == goal: return 0 #not necessary
        queue = collections.deque([(start, 0)])
        seen = set([start])
        while queue:
            num, cnt = queue.popleft()
            if 0 <= num <= 1000:
                cnt += 1
                for i in range(len(nums)):
                    temps = [num + nums[i], num - nums[i], num ^ nums[i]]
                    for temp in temps:
                        if temp == goal:
                            return cnt
                        if temp not in seen: 
                            queue.append((temp, cnt))
                            seen.add(temp)
        return -1
