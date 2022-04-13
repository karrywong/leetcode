class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        #Leetcode's schoolbook addition, much cleaner code
        #Time O(max(len(num), logk)), space O(max(len(num), logk))
        num[-1] += k
        for i in range(len(num)-1,-1,-1):
            carry, num[i] = divmod(num[i], 10)
            if i:
                num[i-1] += carry
        if carry:
             num = list(map(int, str(carry))) + num
        return num
        
#         #First attempt, messy code, time O(max(len(num), logk)), space O(max(len(num), logk))
#         ans = []
#         carry = 0
        
#         i = -1
#         while i >= -len(num) and k:
#             k, r = divmod(k, 10)
#             carry, val = divmod(num[i] + r + carry,10)
#             ans.append(val)
#             i -= 1
        
#         if i >= -len(num):
#             while i >= -len(num):
#                 carry, val = divmod(num[i] + carry,10)
#                 ans.append(val)
#                 i -= 1
#             if carry:
#                 ans.append(carry)
#         elif k:
#             k += carry
#             while k:
#                 k, r = divmod(k, 10)
#                 ans.append(r)
                
#         elif carry: 
#             ans.append(carry)
        
#         return ans[::-1]
