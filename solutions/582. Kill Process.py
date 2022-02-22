class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        #DFS or BFS, time O(N), space O(N)
        graph = collections.defaultdict(set)
        for process_id, process_parent in zip(pid,ppid):
            graph[process_parent].add(process_id)
        
        ids = []
        # def get_process(process_id): #DFS recursion
        #     ids.append(process_id)
        #     for process_child in graph[process_id]:
        #         get_process(process_child)
        # get_process(kill)
​
        # stack = [kill] #DFS iterative
        # while stack:
        #     process_id = stack.pop()
        #     ids.append(process_id)
        #     stack.extend(graph[process_id])
        
        queue = collections.deque([kill]) #BFS
        while queue:
            process_id = queue.popleft()
            ids.append(process_id)
            queue.extend(graph[process_id])
        return ids
