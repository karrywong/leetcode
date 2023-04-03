class Solution {
public:
    double recPower(double x, long long m) {
        if (m == 0)
            return 1.0;
        double half = recPower(x, m/2);
        if (m%2 == 0)
            return half * half;
        else
            return half * half * x;
    }
    
    double myPow(double x, int n) {
        if (x == 0.0) 
            return 0.0;
        long long m = n;
        if (n == 0)
            return 1.0;
        else if (n == 1)
            return x;
        else if (n < 0) {
            x = 1/x;
            m = -m;
        }
        return recPower(x, m);
    }
};
