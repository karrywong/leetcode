class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #eg1,e < r < t < f && w < e  -> w < e < r < t < f
        #attempt 1
        #["wrt","wrf","er", "ett", "rftt"]
        # ans = ["etf", "we"] -> ["wertf"]
        
#         #First attempt in failed mock interview, had not yet learned topological sort
#         #Second attempt after reading CLRS book section 22.4 on topological sort, time O(V+E), space O(V+E)
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        seen = set([char for char in words[0]])
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            j, bd = 0, min(len(w1), len(w2))
            while j < bd and w1[j] == w2[j]:
                j += 1
            if j < bd:
                graph[w1[j]].append(w2[j])
                indegree[w2[j]] += 1
            seen.update([char for char in w2])
            if j == bd and len(w1) > len(w2):
                return ""
            
        queue = collections.deque([char for char in seen if indegree[char] == 0])
        ans = []
        print(queue, seen)
        while queue:
            char = queue.pop()
            ans.append(char)
            
            for nextChar in graph[char]:
                indegree[nextChar] -= 1
                if indegree[nextChar] == 0:
                    queue.append(nextChar)
        return ''.join(ans) if len(ans) == len(seen) else ""
