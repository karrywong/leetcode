from collections import Counter
​
​
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages) # key: num, val: freq
        unique_ages = list(counter.keys())
        ans = 0
        for i in range(len(unique_ages)): # i=1
            age = unique_ages[i] # x=17
            if counter[age] > 1 and age>14: 
                ans += counter[age] * (counter[age]-1)
                
            for another_age in unique_ages[:i] + unique_ages[i+1:]: #y=16
                if age < another_age or  0.5*age+7 >= another_age: #15 <16
                    continue
                ans += counter[age] * counter[another_age]
                
        return ans
        
        # [16,16,17,17,17] -> {16:2, 17:3}, uniques_age=[16,17]
        # ans = 2*1 (among 16s)+3*2 (among 17s)+3*2 (17s->16s) = 14
        
        
        
