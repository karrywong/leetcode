class Solution {
private:
    int ans = INT_MAX;
public:
    void dfs(int start, int end, vector<int>& nums) {
        if (start == end) {
            ans = min(ans, nums[start]);
            return;
        }
        int mid = start + (end-start)/2;
        if (nums[end] >= nums[mid]) dfs(start, mid, nums);
        if (nums[end] <= nums[mid]) dfs(mid+1, end, nums);
    }
    
    int findMin(vector<int>& nums) {
        dfs(0, nums.size()-1, nums);
        return ans;
    // Soln 0 - modified from 153. Find Minimum in Rotated Sorted Array
    //case1 l<= r -> ans = l
    //case2 r < l < mid -> mid = l+1
    //case3 mid < r < l -> mid = r       
    // [l, mid, r] -> [r, l, mid] -> [mid, r, l] -> [l, mid, r]
    //case4 
        // int l = 0, r = nums.size()-1, mid;   
        // while (l < r) {
        //     mid = l + (r-l) / 2; 
        //     if (nums[r] < nums[mid]) l = mid+1;
        //     else if (nums[mid] < nums[r]) r = mid;
        //     else r -= 1;
        // }
        // return nums[l]; 
    }
};
