class Solution {
public:
    int findMin(vector<int>& nums) {
    //case1 l<= r -> ans = l
    //case2 r < l < mid -> mid = l+1
    //case3 mid < r < l -> mid = r       
    // [l, mid, r] -> [r, l, mid] -> [mid, r, l] -> [l, mid, r]
    //case4 
        int l = 0, r = nums.size()-1, mid;   
        while (l < r) {
            mid = l + (r-l) / 2; 
            if (nums[r] < nums[mid]) l = mid+1;
            else if (nums[mid] < nums[r]) r = mid;
            else r -= 1;
        }
        return nums[l]; 
    }
};
​
​
