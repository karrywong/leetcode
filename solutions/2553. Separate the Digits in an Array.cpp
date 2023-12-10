class Solution {
public:
    vector<int> getDigits(int& num) {
        vector<int> vecDigits;
        while (num > 0) {
            int r = num % 10; 
            vecDigits.push_back(r);
            num /= 10;
        }
        return vecDigits; // {3,1}
    }
        
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> ans;
        for (auto& num : nums) {
            vector<int> vecDigits = getDigits(num);
            for (int i=vecDigits.size()-1; i > -1; i--) {
                ans.push_back(vecDigits[i]);
            }
        }
        return ans;
    }
};
