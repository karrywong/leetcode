class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // first attempt, time O(N), space O(1)
        int j=0, temp;
        for (int i=0; i<nums.size(); i++){
            if (nums[i] != 0) {
                swap(nums[j++], nums[i]);
            }
        }
        
    }
};
