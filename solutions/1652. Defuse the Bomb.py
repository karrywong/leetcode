class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # 2nd attempt, cleaner code, time O(n), space O(n)
        n = len(code)
        res = [0] * n
        if k == 0: return res
        elif k < 0:
            k *= -1
            s, e = n-k, n
        else:
            s, e = 1, k+1
        val = sum(code[s:e])
        
        for i in range(n):
            res[i] = val
            val -= code[s%n]
            val += code[e%n]
            s += 1
            e += 1 
        return res
        
#         # sliding window, time O(n), space O(n)
#         n = len(code)
#         k_abs = abs(k)
#         arr = [sum(code[:k_abs])]
#         for i in range(n-1):
#             val = arr[-1]
#             val -= code[i]
#             val += code[(i+k_abs) % n]
#             arr.append(val)
#         return arr[1:]+[arr[0]] if k > 0 else arr[n-k_abs:] + arr[:n-k_abs]
        
            
        
