class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # soln 0 - first attempt, BFS w memoization
        n = len(stickers)
        lib_lst = [None] * n 
        for i in range(n):
            lib_lst[i] = collections.Counter(stickers[i])
        
        lib_target, arr = collections.Counter(target), [0] * 26
        for k, v in lib_target.items():
            arr[ord(k) - ord('a')] = v
        queue = collections.deque([(arr,0)])
        seen = set([tuple(arr)])
        
        while queue:
            temp, count = queue.popleft()
            if sum(temp) == 0: return count
            val = sum(temp)
            
            count += 1
            val2 = val
            for i in range(n):
                temp2 = temp.copy()
                for k,v in lib_lst[i].items():
                    ix = ord(k) - ord('a')
                    if temp2[ix] != 0:
                        if temp2[ix] <= v:
                            temp2[ix] = 0
                        else:
                            temp2[ix] -= v
                val2 = min(val2, sum(temp2))
