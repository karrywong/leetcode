class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Time O(N), space O(N)
        
        # [5,4,2,4], temp = {2,4}
        # [5,4,5,2,4]
        # [5,4,5,4,5,4,2,4], left = index 0, right = 2, search 0,1,2,3,4 -> 
        # [5,4,5,4,5,4,5,3,2,4]
        # [5,4,4,5,4,4,3,1]
        # [5,4,1,8]
        
        left = 0
        ans = 0
        lower_bound = float('-inf')
        upper_bound = float('inf')
        hash_map = {}
        
        for right in range(len(nums)):
            num = nums[right]
            hash_map[num] = right
            
            if lower_bound <= num <= upper_bound:
                ans += right-left+1
                lower_bound = max(num-2, lower_bound)
                upper_bound = min(num+2, upper_bound)
            else:
                #find left
                candidates = set(range(lower_bound, upper_bound+1))
                candidates = candidates.difference(set(range(num-2, num+3)))
                left = -1
                for c in candidates:
                    left = max(hash_map.get(c,-1), left)
                if left == -1:
                    left = right
                    lower_bound = nums[right]-2
                    upper_bound = nums[right]+2
                else:
                    left += 1
                    temp = set()
                    for x in range(nums[right]-2, nums[right]+3):
                        if x in hash_map and hash_map[x] >= left:
                            temp.add(x)
                    lower_bound = max(temp)-2 #4-2=2
                    upper_bound = min(temp)+2 #2+2=4
                ans += right-left+1
                
            # print(num, left, right, ans, lower_bound, upper_bound, hash_map)
        return ans
