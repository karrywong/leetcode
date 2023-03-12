class Solution {
public:
    int findClosestElement(vector<int>& arr, int x) {
        int l=0, r=arr.size()-1; 
        while (l+1 < r) {
            int mid = l + (r-l)/2;
            if (arr[mid] == x) return mid;
            else if (arr[mid] < x) l = mid;
            else r = mid;
        } 
        if (abs(x-arr[r]) < abs(x-arr[l])) return r;
        else return l;
    }
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int h = findClosestElement(arr, x);
        int start = h, end = h;
        while (end-start+1 < k) { 
            if (start == 0) end++;
            else if (end == arr.size()-1) start--;
            else if (x-arr[start-1] <= arr[end+1]-x) start--;
            else end++; 
        }
        vector<int> ans; 
        for (int i = start; i <= end; i++) ans.push_back(arr[i]);
        return ans;
    }
};
