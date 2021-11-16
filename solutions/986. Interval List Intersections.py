class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #soln 0 - first attempt, Time O(min(N, M)), Space O(min(N,M))
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            A, B = firstList[i], secondList[j]
            if not (A[1] < B[0] or A[0] > B[1]):
                #there is an intersection
                ans.append([max(A[0], B[0]), min(A[1], B[1])])
            if A[1] <= B[1]:
                i += 1
            else:
                j += 1
        return ans
        
