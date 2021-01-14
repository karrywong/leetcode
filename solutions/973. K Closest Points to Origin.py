​
#             while True:
#                 while i < j and dist(i) < pivot:
#                     i += 1
#                 while i <= j and dist(j) >= pivot:
#                     j -= 1
#                 if i >= j: break
#                 points[i], points[j] = points[j], points[i]
​
#             points[oi], points[j] = points[j], points[oi]
#             return j
​
#         sort(0, len(points) - 1, K)
#         return points[:K]
        
        # ### Soln 0 - LeetCode O(NlogN) (We should learn from it, lambda!!!):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
        
#         ### Soln 1 - Hashmap O(NlogN), my original attempt
#         lib = {}
        
#         for n in points:
#             dist = n[0]**2 + n[1]**2
#             if dist not in lib:
#                 lib[dist] = [n]
#             else:
#                 lib[dist].append(n)
                
#         res = []
#         lst = [v for v in sorted(lib.keys())]
#         i = 0
#         while K > 0: 
#             k = lst[i]
#             val = len(lib[k])
#             res += lib[k]
            
#             K -= val
#             i += 1
            
#         return res
