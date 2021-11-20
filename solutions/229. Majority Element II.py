class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #soln 1 - Leetcode Boyer-Moore Voting Algorithm
        #Key observation: there can only be two majority elements more than [n/3] times
        ans1, ans2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if count2 == 0 and ans1 != num:
                ans2 = num
                count2 = 1
                continue
            if count1 == 0 and ans2 != num:
                ans1 = num
                count1 = 1
                continue
            if ans1 == num and ans2 is None:
                count1 += 1
            if ans2 == num and ans1 is None:
                count2 += 1            
            
            if ans1 is not None and ans2 is not None:
                if ans1 != num and ans2 != num:
                    count1 -= 1
                    count2 -= 1
                elif ans1 == num and ans2 != num:
                    count1 += 1
                elif ans1 != num and ans2 == num:
                    count2 += 1
                    
        print(ans1, count1, ans2, count2)
        ans, n = [], int(len(nums)/3)
        if ans1 is not None and nums.count(ans1) > n:
            ans.append(ans1)
        if ans2 is not None and nums.count(ans2) > n:
            ans.append(ans2)
        return ans
        
        # #soln 0 - hashtable, Time O(N), Space O(N)
        # n = int(len(nums)/3)
        # lib = collections.defaultdict(int)
        # ans = []
        # for num in nums:
        #     lib[num] += 1
        #     if lib[num] > n and num not in ans:
        #         ans.append(num)
        # return ans
