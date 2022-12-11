class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        // Two pointers, time O(N), space O(N)
        int numsLen = nums.size();
        int r = numsLen-1, l = 0;
        vector<int> ans(numsLen);
        for (int i = numsLen-1; i > -1; i--) {
            if (abs(nums[l]) > abs(nums[r])) {
                ans[i] = nums[l]*nums[l];
                l++;
            }
            else {
                ans[i] = nums[r]*nums[r--];
                r--;
            }
        }
        return ans;
        
        // // trivial, time O(NlogN), space O(N)
        // vector<int> ans;
        // for (auto num : nums) {
        //     ans.push_back(num * num);
        // }
        // sort(begin(ans), end(ans));
        // return ans;
    }
};
