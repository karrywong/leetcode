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
        
        // // Fermat theorem
        // for (int x = 2; x*x <= c; x++) {
        //     if (c % x == 0) {
        //         int count = 0;
        //         while (c % x == 0) {
        //             count++;
        //             c /= x;
        //         }
        //         if (count % 2 != 0 && x % 4 == 3) return false;
        //     }
        // }
        // return c % 4 != 3;
    }
};
