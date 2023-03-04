class Solution {
public:
    int findMin(vector<int>& nums) {
    //case1 l< mid < r -> ans = l
    //case2 r < l < mid -> mid = l+1
    //case3 mid < r < l -> mid = r           
    // [l, mid, r] -> [r, l, mid] -> [mid, r, l] -> [l, mid, r]
    int l = 0, r = nums.size()-1, mid;   
    while (l < r) {
        if (nums[l] < nums[r]) break; //nums[l] > nums[r]
        mid = l + (r-l) / 2; 
        if (nums[l] <= nums[mid]) l = mid+1;
        else r = mid;
    }
    return nums[l];
    }
};
