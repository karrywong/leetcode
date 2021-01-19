class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ### Soln 3 - Leet Code, very clever idea using hashmap to record the last seen letter
#         last = {c: i for i, c in enumerate(S)}
#         # print(last)
#         j = anchor = 0
#         ans = []
#         for i, c in enumerate(S):
#             j = max(j, last[c])
#             if i == j:
#                 ans.append(i - anchor + 1)
#                 anchor = i + 1
#             # print(i,j,anchor,ans)
    
#         return ans
    
        ### Soln 2 - Jake & Karry, Greedy algorithm, optimized
        lastseen = {}
        lengthStack = []
        
        for i,s in enumerate(S):
        
            if s not in lastseen: # record new element and start new partition
                lastseen[s] = i
                lengthStack.append(1)
            else:
                temp = 1 # combinded partition length
                # sum partition lengths from stack until partition contains
                # both s and the previous occurence of s
                while temp < i - lastseen[s] + 1:
                    temp += lengthStack.pop()
                lastseen[s] = i # update lastseen
                lengthStack.append(temp) 
        
        return lengthStack
    
    
        ### Soln 1 - Jake & Karry, Greedy algorithm 
        ### idea: use a set (seen) to keep track of letters and stack the partition
#         seen = set()
#         stack = []
        
#         for s in S:
#             if s not in seen:
