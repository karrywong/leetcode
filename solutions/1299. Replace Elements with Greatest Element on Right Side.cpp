class Solution {
public:
    vector<int> replaceElements(vector<int>& arr, int mx = -1) {
        // C++ exchange, cleaner
        for (int i = arr.size() - 1; i >= 0; --i)
            mx = max(mx, exchange(arr[i], mx));
        return arr;
        
        // // first attempt
        // int maxElement = -1, temp; 
        // for (int i = arr.size()-1; i > -1; i--) {
        //     temp = arr[i];
        //     arr[i] = maxElement;
        //     maxElement = max(temp, maxElement);
        // }
        // return arr;
    }
};
