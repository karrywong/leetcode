class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ### Soln 2 - discussion by lee215
#         wait = cur = 0.
#         for a, t in customers:
#             cur = max(cur, a) + t
#             wait += cur - a
#         return wait / len(customers)
        
        ### Soln 1 - original attempt
        n = len(customers)
        
        curr_time = customers[0][0]
        wait_time = curr_time + customers[0][1] - customers[0][0]
        curr_time += customers[0][1]
        
        for i in range(1, n):
            curr_time = max(curr_time, customers[i][0])
            wait_time += curr_time + customers[i][1] - customers[i][0]
            curr_time += customers[i][1]
        return wait_time / n
​
        
