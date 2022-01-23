class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # #Second attempt, straight forward using queue, time O(N), space O(1)
        # queue = collections.deque(range(1,n+1))
        # while len(queue) > 1:
        #     for i in range(k-1):
        #         queue.append(queue.popleft())
        #     queue.popleft()
        # return queue[0]
        
        #First attempt, time O(N), space O(1)
        lst = [i for i in range(1,n+1)]
        cur, m = k-1, len(lst)
        while m > 1:
            lst.pop(cur)
            m -= 1
            cur += k-1
            cur %= m
        return lst[0]
