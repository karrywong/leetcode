class Solution {
public:
//     int modPow(long long x, long long y, int m)
//     {
//         if (y == 0)
//             return 1;
//         long long p = modPow(x, y / 2, m);
//         p = (p * p) % m;
//         return y % 2 ? (p * (x % m)) % m : p;
//     }    
    
    int minNonZeroProduct(int p) {
//         /* God IC - Vlad */
//         long long cnt = (1ll << p) - 1, mod = 1000000007;
//         return cnt % mod * modPow(cnt - 1, cnt / 2, mod) % mod;
        
        /* Our failed attempt */
        if (p == 1) return 1;
        int mod = int(pow(10,9)+7);
        // int maxVal = int(pow(2,p)-1) % mod;
        long long maxVal = ((1ll << p) - 1) % mod;
        int secMaxVal = (maxVal-1) % mod;
        
        long long ans = secMaxVal;
        long long curProd = secMaxVal;
        for (int i = 1; i < p-1; i++) {
            curProd *= curProd;
            curProd %= mod;
            ans *= curProd;
            ans %= mod;
        }
        return (maxVal* ans) % mod;
    }
};
