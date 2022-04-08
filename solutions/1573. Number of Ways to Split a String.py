class Solution:
    def numWays(self, s: str) -> int:
        #Inspired by explanations provided by rock, time O(N), space O(1)
        s_int = [int(char) for char in s]
        total_val = sum(s_int)
        if total_val % 3 != 0:
            return 0
        elif total_val == 0:
            return (len(s)-1)*(len(s)-2)//2 % (10**9+7)
        else:
            one_third_total_val = total_val//3
            val, check1, check2 = 0, one_third_total_val, 2*one_third_total_val
            count1, count2 = 0, 0
            i = 0
            while i < len(s_int) and val <= check2:
                val += s_int[i]
                if val == check1:
                    count1 += 1
                elif val == check2:
                    count2 += 1
                i += 1
            return (count1 * count2) % (10**9+7)
