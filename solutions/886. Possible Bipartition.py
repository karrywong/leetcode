class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        #Too many failed attempts - no idea how to apply DFS on this problem
#         #Modified soln from graph coloring by brianchiang_t, time O(V+E), space O(V)
#         #Two different colors with opposite sign, i.e. blue = 1 & green = -1
#         if n == 1 or not dislikes:
#             return True
        
#         def can_color(person_id: int, color: int) -> bool:
#             colors[person_id] = color
#             for ngh in dislike_graph[person_id]:
#                 if colors[ngh] == color:
#                     return False
                
#                 if colors[ngh] == 0 and not can_color(ngh, -color):
#                     return False
#             return True
        
        dislike_graph = collections.defaultdict(set)
        colors = [0] * (n+1)
        for u, v in dislikes:
            dislike_graph[u].add(v)
            dislike_graph[v].add(u)
        
#         for i in range(1,n+1):
#             if colors[i] == 0 and not can_color(i, 1):
#                 return False
#         return True
​
        #Soln 2 - much cleaner, by WangQiuc, two colors: 1 and 0
        seen = {}
        def dfs(person_id, color):
            if person_id in seen:
                return seen[person_id] == color
            seen[person_id] = color
            return all(dfs(ngh, 1-color) for ngh in dislike_graph[person_id])
        return all(dfs(i, 0) for i in range(1, n+1) if i not in seen)
