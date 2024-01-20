class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        //initialization
        unordered_map<int, int> seen;
        unordered_set<int> duplicate;
        long long val=0;
        for (int i=0; i<k;i++){
            val += nums[i];
            if (seen.contains(nums[i])) {
                seen[nums[i]] += 1;
                duplicate.insert(nums[i]);
            } else {
                seen[nums[i]] = 1;
            }
        }
        long long ans = duplicate.size() == 0 ? val : 0;
        
        for (int i = k; i < nums.size();i++) {
            seen[nums[i-k]] -= 1;
            if (duplicate.contains(nums[i-k]) && seen[nums[i-k]] <= 1) {
                duplicate.erase(nums[i-k]);
            }
            if (seen.contains(nums[i])) {
                seen[nums[i]] += 1;
            } else {
                seen[nums[i]] = 1;
            }
            
            if (seen[nums[i]] > 1) {
                duplicate.insert(nums[i]);
            }
            
            val -= nums[i-k];
            val += nums[i];
            
            if (duplicate.size() == 0) ans = max(ans, val);
        }
        return ans;
    }
};
