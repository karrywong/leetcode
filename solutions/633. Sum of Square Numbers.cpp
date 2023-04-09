class Solution {
public:
    bool judgeSquareSum(int c) {        
        // Brute-force
        for (int x = 0; x <= floor(sqrt(c/2)); x++) {
            int d = c - x*x;
            int dSqrt = floor(sqrt(d));
            if (dSqrt*dSqrt == d) return true;
        }
        return false;
    }
};
