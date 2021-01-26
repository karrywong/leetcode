class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        # ## Using idea from leetcode solution. Used more memory than 2nd solution
        # S = list(S)
        # d = {indexes[i]:(sources[i],targets[i]) for i in range(len(indexes))}
        # for i in reversed(range(len(S))):
        #     if (i in d) and S[i:i+len(d[i][0])] == list(d[i][0]):
        #         S[i:i+len(d[i][0])] = list(d[i][1])
        # return ''.join(S)
​
        ## Solution by Jake Reschke
        output = []
        d = {indexes[i]:(sources[i],targets[i]) for i in range(len(indexes))}
        i = 0
​
        while i < len(S):
            if i in d:
                source,target = d[i]
                if S[i:i+len(source)] == source:
                    output.append(target)
                    i += len(source)
                else:
                    output.append(S[i])
                    i += 1                       
            else:
                output.append(S[i])
                i += 1
        return ''.join(output)
