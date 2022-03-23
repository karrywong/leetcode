#Leetcode Brute force, time O(1), space O(1)
class Seqs:
    def __init__(self):
        sample = '123456789'
        n = 10
        self.nums = []
        for length in range(2, n):
            for start in range(n-length):
                self.nums.append(int(sample[start:start+length]))
​
class Solution:
    s = Seqs()
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [x for x in self.s.nums if x >= low and x <= high]
        
#         #Leetcode Sliding window, much cleaner, time O(1), space O(1)
#         sample = '123456789'
#         n = 10
#         nums = []
        
#         for length in range(len(str(low)), len(str(high))+1):
#             for start in range(n-length):
#                 num = int(sample[start:start+length])
#                 if low <= num <= high:
#                     nums.append(num)
#         return nums
        
        #First attempt, too complicated, time O(1), space O(1)
#         low_string = str(low)
#         n = len(low_string)
#         lookup = '987654321'
#         compare = int(lookup[:n][::-1])
#         ans = []
        
#         if low <= compare:
#             first_digit = int(low_string[0])
#             compare2 = first_digit # first_digit
#             val = compare2
#             for i in range(n-1):
#                 val *= 10
#                 val += compare2 + 1
#                 compare2 += 1
#             # print(val, compare2)
#             if low > val:
#                 val += int('1' * n)
#         else:
#             val = int(lookup[9-n-1:][::-1])
#             n += 1
            
#         if low <= val <= high:
#             ans.append(val)
        
#         while ans:
#             first_digit = str(ans[-1])[0]
#             if n <= len(lookup) and first_digit >= lookup[n-1]:
#                 val = int(lookup[9-n-1:][::-1])
#                 n += 1
#             else:
#                 val = ans[-1] + int('1' * n)
#             if val < low or val > high:
#                 break
#             ans.append(val)
#         return ans
