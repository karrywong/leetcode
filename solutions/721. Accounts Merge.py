class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #DFS solution from DBabichev in discussion
        names = {}
        graph = defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                names[email] = name
                
        comps, seen, ans, i = defaultdict(list), set(), [], 0
        def dfs(node, i):
            comps[i].append(node)
            seen.add(node)
            for neib in graph[node]:
                if neib not in seen: dfs(neib, i)
        
        for email in graph:
            if email not in seen:
                dfs(email, i)
                i += 1
        return [[names[val[0]]] + sorted(val) for _,val in comps.items()]
    
#         #Jake's solution 
#         accountsMerged = []
#         # Construct a graph where nodes are emails and connected nodes belong to the same user
#         graph = defaultdict(set)
#         for account in accounts:
#             if account[1] not in graph:
#                 graph[account[1]]
#             for i in range(2,len(account)):
#                 graph[account[i]].add(account[i-1])
#                 graph[account[i-1]].add(account[i])
        
#         accountsMerged = []
#         seen = set()
#         for account in accounts:
#             if account[1] not in seen:
#                 emails = []
#                 # initiate DFS 
#                 stack = [account[1]]
#                 seen.add(account[1])
#                 while stack:
#                     cur = stack.pop()
#                     emails.append(cur)
#                     for ngbr in graph[cur]:
#                         if ngbr not in seen:
#                             seen.add(ngbr)
#                             stack.append(ngbr)
#                 emails.sort()
#                 accountsMerged.append([account[0]] + emails)
                
#         return accountsMerged
