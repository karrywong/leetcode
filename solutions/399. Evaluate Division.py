class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #LeetCode soln using Union-Find, time O((M+N)*alpha(N)), space O(N)
        gid_weight = {} #key -> (group_id, weight)
        
        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]
            
            if group_id != node_id:
                #Path compression -> found inconsistency, trigger chain update
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = (new_group_id, node_weight * group_weight)
            return gid_weight[node_id]
        
        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # merge the two groups together, by attaching the dividend group to the one of divisor
                gid_weight[dividend_gid] = (divisor_gid, divisor_weight * value / dividend_weight)
                
        # Step 1 - build the union groups
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)
        # Step 2 - loop over queries, with "lazy" updates in find() function
        results = []
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                results.append(-1.0) #dividend or divisor not yet seen 
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)        
                if dividend_gid != divisor_gid:
                    results.append(-1.0) #no relation available
                else:
                    results.append(dividend_weight / divisor_weight)
        return results
