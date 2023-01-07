class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int maxElement = -1, temp; 
        for (int i = arr.size()-1; i > -1; i--) {
            temp = arr[i];
            arr[i] = maxElement;
            maxElement = max(temp, maxElement);
        }
        return arr;
    }
};
