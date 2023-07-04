class Solution {
public:
    int minimumAverageDifference(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;
        
        long long sum1 = nums[0], sum2 = 0;
        for (int i = 1; i < n; i++) {
            sum2 += nums[i];
        }
        double avgDiff = abs((double)sum1-(double)sum2/(n-1));        
        int ans = 0;
        for (int i = 1; i <= n-1; i++) {
            sum1 += nums[i];
            sum2 -= nums[i];
            double temp = i != n-1 ? abs(sum1 /(i+1) - sum2/(n-i-1)) : sum1/n;
            if (temp < avgDiff) {
                ans = i;
                avgDiff = temp;
            } 
        }
        return ans;
    }
};
​
// Sa + Sb = sum(nums)
// | Sa / a - Sb / b | 
// | (Sa + x)/(a+1) - (Sb-x)/(b-1) | 
​
// [12, 12, 19, 14, 16]
