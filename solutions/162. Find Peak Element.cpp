class Solution {
public:
    int findPeakElement(vector<int>& nums) {
    // mid -> if nums[mid] is peak
    // yes -> return
    // no -> max(nums[mid-1], nums[mid+1]) -> l, r update
    int l = 0, r = nums.size()-1;
    while (l < r) {
        int mid = l + (r-l)/2;
        if (nums[mid] < nums[mid+1]) l = mid+1;
        else r = mid;
    }
    return l;
    }
};
