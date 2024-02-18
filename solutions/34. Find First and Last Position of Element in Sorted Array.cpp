class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans;
        int l = 0, r = nums.size()-1;
        while (l < r ) {
            int mid = l + (r-l)/2;
            if (nums[mid] < target) l = mid+1;
            else r = mid;
        } 
        if (r == -1 || nums[l] != target) return {-1,-1};
        ans.push_back(l);
        
        l = 0;
        r = nums.size();
        while (l < r) {
            int mid = l + (r-l)/2;
            if (nums[mid] > target) r = mid;
            else l = mid+1; 
        } 
        ans.push_back(l-1);
        return ans;
    }
};
