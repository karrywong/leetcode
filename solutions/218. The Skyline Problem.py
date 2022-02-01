        # points.sort()
        # pq, max_height = [0], 0
        # key_points = []
        # for x, h, s in points:
        #     if s == 1: # start point
        #         if -h > max_height:
        #             max_height = -h
        #             key_points.append([x, -h])
        #         bisect.insort_right(pq, -h)
        #     else: # end point
        #         pq.pop(bisect.bisect_left(pq, h))
        #         pq_max = pq[-1]
        #         if pq_max < max_height:
        #             max_height = pq_max
        #             key_points.append([x, max_height])
        # return key_points
    
        #Failed attempts due to too many edge cases...
        # cleaned = [buildings[0]]
        # for i in range(1,len(buildings)):
        #     if cleaned[-1][0] == buildings[i][0] and cleaned[-1][1] == buildings[i][1]:
        #         cleaned[-1][2] = max(cleaned[-1][2], buildings[i][2])  
        #     elif cleaned[-1][0] <= buildings[i][0] <= cleaned[-1][1] and cleaned[-1][2] == buildings[i][2]:
        #         cleaned[-1][1] = max(cleaned[-1][1],buildings[i][1])
        #     else:
        #         cleaned.append(buildings[i])
        # pts = []
        # startPt = {}
        # endPt = {}
        # for building in cleaned:
        #     s, e, h = building
        #     startPt[s] = h
        #     endPt[e] = h
        #     pts.extend([s,e])
        # pts.sort()
        # heights = set()
        # maxh = float('-inf')
        # ans = []
        # for pt in pts:
        #     if pt in startPt:
        #         heights.add(startPt[pt])
        #         if startPt[pt] > maxh:
        #             maxh = startPt[pt]
        #             ans.append([pt, maxh])
        #     if pt in endPt: 
        #         if endPt[pt] in heights:
        #             heights.remove(endPt[pt])
        #         if len(heights) >= 1 and endPt[pt] == maxh:
        #             maxh = max(heights)
        #             ans.append([pt, maxh])
        #         elif len(heights) == 0:
        #             ans.append([pt,0])
        #             maxh = float('-inf')
        # return ans
