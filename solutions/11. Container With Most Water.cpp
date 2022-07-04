class Solution {
public:
    int maxArea(vector<int>& height) {
        //cleaner code from vipkk67
        int ans = INT32_MIN;
        for (int i = 0, j = height.size() - 1; i < j;) {
            ans = max(ans, (j-i) * min(height[i], height[j]));
            height[i] < height[j] ? i++ : j--;
        }
        return ans;
            
        // int ans = 0, l = 0, r = height.size()-1;
        // while (l < r) {
        //     int width = r - l, temp;
        //     if (height[l] < height[r]) {
        //         temp = height[l] * width;
        //         l += 1;
        //     } else {
        //         temp = height[r] * width;
        //         r -= 1;                
        //     }
        //     ans = max(ans, temp);
        // }
        // return ans;
    }
};
