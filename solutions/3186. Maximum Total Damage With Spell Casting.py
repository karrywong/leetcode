from collections import Counter
​
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        #[1,3,4]
        # 1 -> 4 = 5
        # 3  = 3
        
        # [5,5,1,...,1,2,3,4,]
        # sorting O(NlogN)
        # number -> value
        # [(1:10), (2:2), (3:0), (4:4), (5:10)]
        
        #nums = [(1:10), (2:2), (3:x), (100:100)]
        
        counter = Counter(power)
        nums = sorted(list(counter.keys()))
        
        rob, not_rob, notnot_rob = nums[0]*counter[nums[0]],0,0
        prev_seen = nums[0]
        # print(nums)
        for num in nums[1:]:
            val = num*counter[num]
            if num-prev_seen <= 1:
                rob, not_rob, notnot_rob = max(notnot_rob+val, not_rob, rob), max(notnot_rob, not_rob, rob), max(notnot_rob, not_rob)
            elif num-prev_seen == 2:
                rob, not_rob, notnot_rob = max(notnot_rob+val, not_rob+val, rob), max(notnot_rob, not_rob, rob), max(notnot_rob, not_rob, rob)    
            else: # >= 3
                gain = max(rob, not_rob, notnot_rob)
                notnot_rob = gain
                not_rob = gain
                rob = gain+val
            # print(f"{num=},{rob=}, {not_rob=}, {notnot_rob=}")             
            prev_seen = num
        return max(rob, not_rob, notnot_rob)
        
        #  = [{1,4},{3}]
        # return max(sum(p) for p in possible)
        
        # for over power
        #     for over possible # O()
        
