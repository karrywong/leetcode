class Solution {
public:
    int meetRequirement(int n, vector<vector<int>>& lights, vector<int>& requirement) {
        // n = 5, [0, 4]
        //  [[0,1],[2,1],[3,2]] -> [[0,1], [1,3], [1,4]]        
        // change in brightness [1, 2, -1, 0, -1]
        // [0,2,1,4,1]
        
        // [0,1], [2,1], [3,2]
        // [ 1, 2, -1, 0, -1]
        // [T,T,T,F,T]
        
        vector<int> brights(n,0); //change in brightnesss
        for (auto& l: lights) {
            int s = max(0, l[0]-l[1]), e = min(n-1, l[0]+l[1]);
            brights[s]++;
            if (e+1 <= n-1) brights[e+1] -= 1; 
        }
        
        int ans = 0, val = 0;
        for (int i=0; i<requirement.size(); ++i){
            val += brights[i];
            if (val >= requirement[i]) ans++;
        }        
        return ans;
        
    }
};
