class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long firstMax = numeric_limits<long>::min();
        long secondMax = numeric_limits<long>::min();
        long thirdMax = numeric_limits<long>::min();;
        for (const auto& num : nums) {
            if (num > firstMax ) {
                thirdMax = secondMax;
                secondMax = firstMax;
                firstMax = num;
            }
            else if (num == firstMax) continue;
            else if (num > secondMax) {
                thirdMax = secondMax;
                secondMax = num;
            }
            else if (num == secondMax) continue;
            else if (num > thirdMax) thirdMax = num;
        }
        return thirdMax == numeric_limits<long>::min() ? firstMax : thirdMax;
        
    }
};
