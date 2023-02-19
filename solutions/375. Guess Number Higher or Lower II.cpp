class Solution {
public:
    int tb[201][201]={0};
    // helper(a,b) -> minCost
    int helper(int a, int b) {
        if (tb[a][b] > 0) return tb[a][b];
        int ans = INT_MAX;
        if (a == b) ans = 0;
        else if (a == b-1) ans = a;
        else if (a == b-2) ans = a+1;
        else {
            for (int firstGuess = (a+b)/2; firstGuess < b; ++firstGuess) {
                int cost = firstGuess + max(helper(a, firstGuess-1), helper(firstGuess+1, b));
                ans = min(ans, cost);
            } 
        }
        tb[a][b] = ans;
        return ans;
    }
    int getMoneyAmount(int n) {        
        return helper(1, n);
    }
};
