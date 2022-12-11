class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        // better, time O(n), space O(1)
        int ans = 0, count = 0;
        for (auto num : nums) {
            if (num) {
                count++;
                ans = max(ans, count);
            }
            else count = 0;
        }
        return ans;
​
        // // 1st attempt, time O(n), space O(1)
        // int j = -1;
        // int ans = 0;
        // int len = nums.size();
        // for (int i = 0; i < len; ++i) {
        //     if (nums[i] == 0) {
        //         ans = max(ans, i-j-1);
        //         j = i;
        //     }
        // }
        // ans = max(ans, len-j-1);
        // return ans;
    }
};
