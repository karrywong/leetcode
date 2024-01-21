class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        // nums = [5,0,1,2,3,4]
        // r = nums[i], b = nums[nums[i]] % q, nums[i]=q*b+r
        
        // time O(N), space O(1)
        for (int i=0; i<nums.size(); ++i){
            nums[i] += nums.size()*(nums[nums[i]] % nums.size());
        }
        for (int i=0; i<nums.size(); ++i){
            nums[i] /= nums.size();
        }
        return nums;
    }
};
