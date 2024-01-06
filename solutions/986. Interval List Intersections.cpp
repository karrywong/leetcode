class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        // time O(N+M), space O(1)
        int i=0, j=0;
        vector<vector<int>> ans;
        
        while (i<firstList.size() && j<secondList.size()) {
            int s1=firstList[i][0], e1=firstList[i][1], s2=secondList[j][0], e2=secondList[j][1];
            if (s2 <= e1 && s1 <= e2) {
                ans.push_back({max(s1, s2), min(e1, e2)});
            }
            
            if (e1 <= e2) i++;
            else j++;
        }
        return ans;
    }
};
