class Solution {
public:
    // Solution by votrubac
    // time O(N), space O(N)
    int maximumSum(vector<int>& nums) {
        unordered_map<int, int> lookup; 
        int ans = -1;
        for (const auto num : nums) {
            int digitSum = 0;
            for (int x = num; x; x/=10) {
                digitSum += x % 10;
            }
            if (lookup.contains(digitSum)) {
                ans = max(ans, lookup[digitSum] + num);
                lookup[digitSum] = max(lookup[digitSum], num);
            }
            else {
                lookup[digitSum] = num;
            }
        }
        return ans;
    }
};
