class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        if (arr.size() < 3) return false;
        // strictly increasing
        int i = 1;
        for (; i < arr.size(); ++i) {
            if (arr[i-1] == arr[i])
                return false;
            else if (arr[i-1] > arr[i])
                break;
        }
        
        if (i==1 || i==arr.size()) return false;
        
        // strictly decreasing
        for (; i < arr.size(); ++i) {
            if (arr[i-1] <= arr[i])
                return false;
        }
        
        return true;
    }
};
