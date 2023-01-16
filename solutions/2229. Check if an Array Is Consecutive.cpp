class Solution {
public:
    bool isConsecutive(vector<int>& nums) {     
        // 
        //1^2+2^2+... +n^2 = 1/6 * n*(n+1)*(2n+1) 
        // a^2 + (a+1)^2 + ... +(a+n)^2 = 
        
        // 1st soln, time O(N), space O(N)
        int minNum = *min_element(nums.begin(), nums.end());
        int maxNum = minNum+nums.size()-1;
        bool arr[nums.size()];
        for (auto &a:arr) {
            a = false;
        }
        
        for (const auto num:nums) {
            if (num < minNum || num > maxNum) 
                return false;
            if (arr[num-minNum])
                return false;
            arr[num-minNum] = true;
        }
        return true;
    }
};
