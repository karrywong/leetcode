class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Time O(N), space O(N)
        
        # [5,4,2,4], temp = {2,4}
        # [5,4,5,2,4]
        # [5,4,5,4,5,4,2,4], left = index 0, right = 2, search 0,1,2,3,4 -> 
        # [5,4,5,4,5,4,5,3,2,4]
        # [5,4,4,5,4,4,3,1]
        # [5,4,1,8]

        # shorter sliding window soln, inspired by votrubac
        hash_map = {} #max size of 5 elements
        left_ind = 0
        ans = 0
        for right_ind, num in enumerate(nums):
            hash_map[num] = right_ind
            
            deleted_list = []
            for k, idx in hash_map.items():
                if abs(num-k) > 2:
                    left_ind = max(left_ind, idx+1)
                    deleted_list.append(k)
            
            for d in deleted_list:
                del hash_map[d]
                    
            ans += right_ind - left_ind + 1
        return ans

        
# long long continuousSubarrays(vector<int>& nums) {
#     map<int, int> m;
#     long long res = 0;
#     for (int i = 0, j = 0; i < nums.size(); ++i) {
#         auto [it, inserted] = m.insert({nums[i], i});
#         if (!inserted)
#             it->second = i;
#         else {
#             for (auto it1 = begin(m); nums[i] - it1->first > 2;) {
#                 j = max(j, it1->second + 1);
#                 m.erase(it1++);
#             }
#             for (auto it1 = prev(end(m)); it1->first - nums[i] > 2;) {
#                 j = max(j, it1->second + 1);
#                 m.erase(it1--);
#             }
#         }
#         res += i - j + 1;
#     }
#     return res;
# }
        
        
#         # Attempt 1 - sliding window
#         left = 0
#         ans = 0
#         lower_bound = float('-inf')
#         upper_bound = float('inf')
#         hash_map = {}
        
#         for right in range(len(nums)):
#             num = nums[right]
#             hash_map[num] = right
            
#             if lower_bound <= num <= upper_bound:
#                 ans += right-left+1
#                 lower_bound = max(num-2, lower_bound)
#                 upper_bound = min(num+2, upper_bound)
#             else:
#                 #find left
#                 candidates = set(range(lower_bound, upper_bound+1))
#                 candidates = candidates.difference(set(range(num-2, num+3)))
#                 left = -1
#                 for c in candidates:
#                     left = max(hash_map.get(c,-1), left)
#                 if left == -1:
#                     left = right
#                     lower_bound = nums[right]-2
#                     upper_bound = nums[right]+2
#                 else:
#                     left += 1
#                     temp = set()
#                     for x in range(nums[right]-2, nums[right]+3):
#                         if x in hash_map and hash_map[x] >= left:
#                             temp.add(x)
#                     lower_bound = max(temp)-2 #4-2=2
#                     upper_bound = min(temp)+2 #2+2=4
#                 ans += right-left+1
                
#             # print(num, left, right, ans, lower_bound, upper_bound, hash_map)
#         return ans
