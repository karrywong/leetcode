class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        // vector instead of unordered_set, time O(N), space O(N)
        bool arr[nums.size()+1];
        for (int i=0; i <= nums.size(); i++) {
            arr[i] = false;
        }
        for (const int num : nums) {
            arr[num] = true;
        }
        vector<int> ans;
        for (int i=1; i <= nums.size(); i++){
            if (!arr[i]) ans.push_back(i);
        }
        return ans;
    }
};
