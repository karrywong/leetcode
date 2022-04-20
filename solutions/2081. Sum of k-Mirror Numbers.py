class Solution:
    def kMirror(self, k: int, n: int) -> int:
        #Soln by ye15
        #<https://leetcode.com/problems/sum-of-k-mirror-numbers/discuss/1589048/Python3-enumerate-k-symmetric-numbers>
        def fn(x):
            """Return next k-symmetric number."""
            n = len(x)//2
            for i in range(n, len(x)): 
                if int(x[i])+1 < k: 
                    x[i] = x[~i] = str(int(x[i])+1)
                    for ii in range(n, i): 
                        x[ii] = x[~ii] = '0'
                    return x
            return ["1"] + ["0"]*(len(x)-1) + ["1"]
                
        x = ["0"]
        ans = 0
        for _ in range(n): 
            while True: 
                x = fn(x)
                val = int("".join(x), k)
                if str(val)[::-1] == str(val): break
            ans += val
        return ans 
        
#         #1-9 -> all palindromic
#         #10-99 -> "xx", 1<= x<= 9
#         #100 - 999 -> yxy for x = 0 to 9, for y =  1 to 9
#         #1000 - 9999 -> yxxy  for x = 0 to 9, for y =  1 to 9
#         #5 digits -> zyxyz, for x = 0 to 9, for y =  0 to 9, for z = 1 to 9
        
#         # d digit number = [x1, x2, ..., xd]
#         # 2d palindrome = [xd, xd-1, ..., x1, x1 ..., xd]
#         #(2d-1) palindrome = [xd, xd-1, ..., x2, x1, x2, ...., xd]
        
#         #idea -> 1. generate 10-base palindrome effectively using hints 2. check if palindromic in base-k
        
#         #first attempt - TLE
#         def checkBasek(num): #6, 2 -> [0, 1, 1]
#             baseK = []
#             while num:
#                 num, r = divmod(num,k)
#                 baseK.append(r)
#             return baseK == baseK[::-1]
                
#         ans = 0
#         digits = 1
#         x, y = 1, 0
#         temp = [0]
        
#         while n:            
#             temp[0] += 1
#             if temp[0] == 10:
#                 i = 0
#                 while i < len(temp)-1 and temp[i] == 10:
#                     temp[i] = 0
#                     temp[i+1] += 1
#                     i += 1
            
#             if digits % 2 == 1:
#                 lst = temp[1:][::-1] + temp
#                 num = sum(10**(digits-i-1)*val for i, val in enumerate(lst))
#             else:
#                 lst = temp[::-1] + temp
#                 num = sum(10**(digits-i-1)*val for i, val in enumerate(lst))
            
#             #convert lst into an integer num
#             if checkBasek(num):
#                 n -= 1
#                 ans += num
            
#             if all([a == 9 for a in temp]):
#                 digits += 1
#                 temp = [0] * ceil(digits/2)
#                 if len(temp) > 1: 
#                     temp[0] = -1
#                     temp[-1] = 1
#             # print(digits, lst, num, temp)
            
#         return ans
