class Solution {
public:
    int rob(vector<int>& nums) {
        // i-th house, rob it -> $A, not rob it -> $B
        int rob = 0, notRob = 0, notRobPrev;
        for (const int num : nums) {
            notRobPrev = notRob;
            notRob = rob;
            rob = max(notRobPrev + num, notRob);
        }
        return max(rob, notRob);
        
        // nums = [1,2,3,1]
        // num = 1, R = 1, N = 0, ans = 1
        // num = 2, R = 2, N = 1, ans = 2
        // num = 3, R = 4, N = 2, ans = 4
        // num = 1, R = 3, N = 
    } 
};
