class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        #Mock interview, straight forward soln with minor mistakes, within 30 min
        
        #sort using x-coordinate, [A,B,C,D]
        # find length of AB, AC, BD, CD
        # dot(vec(AB), vec(AC)), dot(vec(AC), vec(CD)) , dot(vec(CD), vec(BD)), dot(vec(AB), vec(BD))
        #return AB == AC == BD == CD and dot products == 0 
        
        length = lambda p,q : (p[0]-q[0])*(p[0]-q[0]) + (p[1]-q[1])*(p[1]-q[1])
        vec = lambda p,q: (p[0]-q[0], p[1]-q[1])
        dot = lambda vec1, vec2: vec1[0]*vec2[0] + vec1[1]*vec2[1]
        A,B,C,D = sorted([p1,p2,p3,p4]) #O(1)
        # print(A,B,C,D)
        ab = length(A,B) #1
        bd = length(B,D) #
        cd = length(C,D)
        ac = length(A,C)
        
        AB = vec(A,B)
        AC = vec(A,C)
        BD = vec(B,D)
        CD = vec(C,D)
        dotA = dot(AB,AC)
        dotB = dot(AB,BD)
        dotC = dot(AC,CD)
        dotD = dot(BD,CD)
        
        return ab > 0 and ab==bd==cd==ac and dotA==dotB==dotC==dotD==0
