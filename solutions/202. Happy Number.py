class Solution:
    def isHappy(self, n: int) -> bool:
        #soln 1 - My version of Floyd's cycle finding algorithm, Space O(logN)
        def get_next(number):
            digits = [int(s) for s in str(number)]
            return sum([i*i for i in digits])
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
        
        # #soln 0 - first attempt, hashtable, Space O(logN)
        # seen = set([n])
        # val = n
        # while val != 1:
        #     digits = [int(s) for s in str(val)]
        #     val = sum([i*i for i in digits])
        #     if val in seen:
        #         return False
        #     seen.add(val)
        # return True
