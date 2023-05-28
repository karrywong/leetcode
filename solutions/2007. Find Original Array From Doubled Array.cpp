class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) { 
        // I - brute force
        // 1. Choose(n, n/2) -> O(n^(n/2)), 2. check O(n)
        // II - sorting time O(NlogN), space O(N)
        // [1,2,3,4,6,8], 
        // ans = [1,]
        
        // [1,1,2,2,2]
        // ans = [1,1], count = {2: 0, } 
        // [1,2,2,3]
        // ans = [1,3], count = {2:-1, 6:1}
        // [0,0,0,0]
        // ans = [0,0], count = {0:1}
        
        if (changed.size() % 2) return {};
        
        sort(changed.begin(), changed.end());
        unordered_map<int,int> count;
        vector<int> ans;
        for (const int x : changed) {
            if (count.find(x) != count.end() && count[x] > 0) count[x] -= 1;
            else {
                ans.push_back(x);
                count[2*x] += 1;
            }
        }
        for (const auto& [_, val] : count){
            if (val != 0) return {};
        }
        return ans;
    }
};
