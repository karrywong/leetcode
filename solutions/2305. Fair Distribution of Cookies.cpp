//Time complexity: O(k^n) w/ n = cookies.size()
class Solution {
public:
    int ans = INT_MAX;
    void solve(int start, vector<int>& cookies, vector<int>& v, int k){
        if (start == cookies.size()) {
            int temp = INT_MIN;
            for (int i = 0; i < k; ++i){
                temp = max(temp, v[i]);
            }
            ans = min(ans,temp);
            return;
        }
        
        for (int i = 0; i < k; ++i) {
            v[i] += cookies[start];
            solve(start+1, cookies, v, k);
            v[i] -= cookies[start];
            if(v[i] == 0) break;
        }
    }
    
    int distributeCookies(vector<int>& cookies, int k) {
        vector<int> v(k,0);
        solve(0, cookies, v, k);
        return ans;
    }
};
