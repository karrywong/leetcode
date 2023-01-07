class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // Soln 1 - two pointer, time O(N), space O(1)
        int j=0;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[j] != nums[i]) {
                nums[++j] = nums[i];
                // OR
                // j++;
                // nums[j++] = nums[i];
            }
        }
        return j+1;
        
        // //Soln 2 - reverse
        // const auto it = std::unique(nums.begin(), nums.end());
        // nums.erase(it, nums.end());
        // return nums.size();
    }
};
