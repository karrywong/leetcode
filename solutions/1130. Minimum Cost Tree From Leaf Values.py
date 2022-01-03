class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        #eg [3,2,1,4], ans = 2+6+12
        # stack = [4]
        # num = 4, prev_small_num = 1, ans += 1 * min(2,4) 
        # prev_small_num = 2, ans += 2 * min(3,4) = 6
        # prev_small_num = 3, ans += 3*4 = 12
​
        #soln by phaniram28 in discussion, time O(N), space O(N)
        """
        idea is to access the smallest value and evict it, since it would not be useful
        for any subsequent operation, while evicting multiply it with smaller neighbor and
        add it to result
        """
        stack = []
        n = len(arr)
        result = 0
        for i in range(n):
            num = arr[i]
            
            while stack and stack[-1] <= num: #keep popping all small elements
                prev_small_num= stack.pop()
                #calculate the non leaf node
                if stack:
                    result += prev_small_num * (min(stack[-1], num))
                else: 
                    result += prev_small_num *num
            stack.append(num)
            
        while stack:
            prev_small_num = stack.pop()
            if stack: result += prev_small_num * stack[-1]
        return result
