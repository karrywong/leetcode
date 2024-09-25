class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ###LeetCode BFS, time O(N^2*A^N+D), where A is #digits in alphabet, N #digits in the lock, D = len(deadends)
        # def neighbors(node):
        #     for i in range(0,4):
        #         x = int(node[i])
        #         for d in (-1, 1):
        #             y = (x + d) % 10
        #             yield node[:i] + str(y) + node[i+1:]
        
        def get_neighbors(node:str) -> List[str]:
            res = []
            for i in range(4):
                digit = int(node[i])
                for change in (-1,1):
                    new_digit = (digit + change) % 10
                    res.append(node[:i] + str(new_digit) + node[i+1:])
            return res
        
        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            # for nei in neighbors(node): # yield
            neighbors = get_neighbors(node)
            for nei in neighbors:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
    
