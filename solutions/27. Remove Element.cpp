class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int ans = 0, j = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[j] = nums[i];
                j++, ans++;
            }
        }
        return ans;
        
        //one-liner by dreyri
        // return std::distance(nums.begin(), std::remove(nums.begin(), nums.end(), val));
    }
};
