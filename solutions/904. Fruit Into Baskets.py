class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ## Soln 2 - from discussion by gralance
        res = cur = count_b = 0
        a = b = -1
        for i, c in enumerate(tree):
            if c == a:
                cur = cur + 1 # extend anser if c is a or b                
                count_b = 1 # reset count of b
                a, b = b, c # let b = c and a be ready to fade out
            elif c == b:
                cur = cur + 1 # extend anser if c is a or b
                count_b = count_b + 1 # add count of b
            else: # new key
                if cur > res: res = cur # update longest result
                cur = count_b + 1  # new answer should count the amount of b and itself
                count_b = 1 # reset count of b
                a, b = b, c # shift left, consider it's a queue.popleft()
​
            # print(i, c, [a, b], [count_b, cur, res])
            
        if cur > res: res = cur # update the remained result
        return res
        
        
#         ### Soln 0 - solution by Jake Reschke
#         left = 0
#         Fruits = set([tree[0]])
#         max_length = 1
#         cur_length = 1
#         for right in range(1,len(tree)):
#             if tree[right] not in Fruits:
#                 Fruits.add(tree[right])
#             if len(Fruits) <= 2:
#                 cur_length += 1
#                 if tree[right]!= tree[right-1]:
#                     left = right -1
#             else:
#                 cur_length = right - left
#                 Fruits.discard(tree[left])
#                 left = right -1
#             max_length = max(max_length,cur_length)
#         return max_length
​
​
#         ### Soln 1 - LeetCode soln w/ sliding window, Time complexity O(n)
