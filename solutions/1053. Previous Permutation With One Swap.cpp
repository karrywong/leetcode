class Solution {
public:
    vector<int> prevPermOpt1(vector<int>& arr) {
        int i = arr.size()-2;
        while (i >= 0 && arr[i] <= arr[i+1]) {
            i -= 1;
        }
        if (i>=0) {
            int max_ = i+1;
            for (int j=i+2; j<arr.size(); j++) {
                if (arr[max_] < arr[j] && arr[j] < arr[i]) {
                    max_ = j;
                }
            }
            swap(arr[max_], arr[i]);
        }
        return arr;
    }
};
