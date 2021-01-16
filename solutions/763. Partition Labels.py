class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ### Soln 2 - Leet Code, very clever idea using hashmap to record the last seen letter
        last = {c: i for i, c in enumerate(S)}
        # print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            # print(i,j,anchor,ans)
    
        return ans
    
        ### Soln 1 - Jake & Karry, Greedy algorithm 
        ### idea: use a set (seen) to keep track of letters and stack the partition
#         seen = set()
#         stack = []
        
#         for s in S:
#             if s not in seen:
#                 seen.add(s)
#                 stack.append([s,1])
#             else:
#                 tempseen = []
#                 tempcount = 1
#                 lastPartition = stack.pop()
​
