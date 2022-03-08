        #Cho's solution, time O(n^2), space O(n)
        w = list(range(n))
        def find(x):
            if w[x] != x:
                w[x] = find(w[x])
            return w[x]
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            w[rootx] = rooty
​
        friends = [set([i]) for i in range(n)]
        not_friends = [set() for _ in range(n)]
        for u, v in restrictions:
            not_friends[u].add(v)
            not_friends[v].add(u)
​
        ans = []
        for u, v in requests:
            x = find(u)
            y = find(v)
            if x == y:
                ans.append(True)
            elif (friends[x].intersection(not_friends[y])) or (friends[y].intersection(not_friends[x])):
                ans.append(False)
            else:
                friends[x].update(friends[y])
                not_friends[x].update(not_friends[y])
                w[y] = x
                ans.append(True)
​
        return ans
        
#         #Union-Find soln, time complexity O(requests * restrictions), space O(n)
#         no_friend = collections.defaultdict(set)
#         for u, v in restrictions:
#             no_friend[u].add(v)
#             no_friend[v].add(u)
          
#         ans = []
#         uf = UnionFind(n)
#         for u, v in requests:
#             rootu = uf.find(u)
#             rootv = uf.find(v)
            
#             approved = True
#             #Check if same root
#             if rootu == rootv:
#                 ans.append(approved)
#                 continue
            
#             #Check each restriction
#             for x, y in restrictions:
#                 rootx, rooty = uf.find(x), uf.find(y)
#                 if (rootu, rootv) == (rootx, rooty) or (rootu, rootv) == (rooty, rootx):
#                     approved = False
#                     break            
            
#             #Not same root
#             if approved:
#                 uf.union(u,v)
#             ans.append(approved)
#         return ans
