class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ### Soln 2 - Divide and Conquer, LeetCode O(N), with the help of Jake Reschke
        L = len(points)
        
        #corner case
        if L == 0 or K == 0: return []
        if L == 1: return points
​
        i = randrange(1,L)
        randPoint = points[i]
​
        leftBin = []
        rightBin = []
​
        # sort elements into left and right bins
        for j in range(0,L):
            if j == i:
                continue
​
            temp = points[j]
​
            if temp[0]**2 + temp[1]**2 < randPoint[0]**2 + randPoint[1]**2:
                leftBin.append(temp)
            else:
                rightBin.append(temp)
​
        # if left bin empty add skipped number, else add to right
        # This ensures that both bins are nonempty and disjoint
        if len(leftBin) == 0:
            leftBin.append(randPoint)
        else:
            rightBin.append(randPoint)
