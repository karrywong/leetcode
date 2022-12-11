class Solution {
public:
    int findNumbers(vector<int>& nums) {
        //1st attempt, time O(n), space O(max(# digits of largest num))
        int ans = 0;
        for (auto num : nums) {
            string numStr = to_string(num);
            if (numStr.size() % 2 == 0) ans += 1;
        }
        return ans;
    }
};
