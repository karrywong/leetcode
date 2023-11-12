class Solution {
public:
    int brightestPosition(vector<vector<int>>& lights) {
        // First, lights = [[-3,2],[1,2],[3,3]] -> ranges = [[-5,-1], [-1,3], [0, 6]] 
        // Second, starts = [-5,-1,0], ends = [-1,3,6]
        // two pointers, ans = (2, -1), count = 1
        
        // Complexity O(NlogN) with N = lights.size()
        vector<int> left, right;
        for (auto light:lights) {
            int pos = light[0];
            int r = light[1];
            left.push_back(pos-r);
            right.push_back(pos+r);
        }
        
        sort(left.begin(), left.end());
        sort(right.begin(), right.end());
        
        //two pointers
        pair<int, int> ans; //(count, position)
        ans = make_pair(0, left.front());
        
        int i=0, j=0, count=0;
        while (i < lights.size()) {
            if (left[i] <= right[j]) {
                count += 1;
                if (count > ans.first) {
                    ans.first = count;
                    ans.second = left[i];
                }
                i += 1;
            } else {
                count -= 1;
                j += 1;
            }
        }
        
        return ans.second;
    }
};
