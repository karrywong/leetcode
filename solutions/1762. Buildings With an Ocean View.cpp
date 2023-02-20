class Solution {
public:
    // [4,2,3,1]
    // [4,3,3,1], ans = [3,2,0]
    vector<int> findBuildings(vector<int>& heights) {
        int n=heights.size();
        vector<int> ans;
        int maxSeen = heights[n-1];
        ans.push_back(n-1);
        for (int i = n-2; i >= 0; i--) {
            if (heights[i] > maxSeen) {
                ans.push_back(i);
                maxSeen = heights[i];
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
