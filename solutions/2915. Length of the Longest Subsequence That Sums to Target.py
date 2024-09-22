class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        #                     0 1 2 3 4 5    9
        # [0] * (target+1) = [0,1,1,2,1,1... 0]
        # target[x] = maximal number of elements that sum to x
        # num > target, continue
​
        # time O(N^2), space constant
        lookup = [0] * (target+1)
        # lookup[0] = 1 (elegant trick -> return lookup[target]-1)
        for idx, a in enumerate(nums): 
            if a > target:
                continue
            
            # hash_map = {} # key: x, value: updated number of elements that sum to x
            # for b, cnt in enumerate(lookup):
            #     if cnt == 0 or a+b > target: 
            #         continue
            #     hash_map[a+b] = cnt+1 
            # for k, v in hash_map.items():
            #     lookup[k] = max(lookup[k], v)
            
            for b in range(target, -1, -1):
                if lookup[b] == 0 or a+b > target: 
                    continue
                lookup[a+b] = max(lookup[b]+1, lookup[a+b])
            
            lookup[a] = max(1, lookup[a])
        return lookup[target] if lookup[target] > 0 else -1
    
    # Testing
    # nums = [1,2,3,4,5], idx = 4
    #  0 1 2 3 4 5 6 7 8 9
    # [0,1,1,0,0,0,0,0,0,0]
​
    #           |
    # nums = [1,1..,1,2], target=10
    #           0 1 2 3 4
    # lookup = [0,1,2,0,0..., 0]
