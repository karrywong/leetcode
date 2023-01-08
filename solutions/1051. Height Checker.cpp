class Solution {
public:
    int heightChecker(vector<int>& heights) {        
        // time O(max(heights)), space O(max(heights))
        int freq[101]={0};
        for (const auto h:heights) {
            freq[h] += 1;
        }
        int ans=0, ind=0;
        for (int i=1; i<101; i++) {
            if (freq[i] != 0) {
                for (int j=0; j<freq[i]; j++) {
                    if (heights[ind++] != i) ans++;
                }
            }
        }
        return ans;
        
//         // 1st attempt, time O(NlogN), space O(N)
//         auto heightsSorted = heights;
//         sort(heightsSorted.begin(), heightsSorted.end());
        
//         int ans = 0;
//         for (int i=0; i<heights.size(); i++){
//             if (heights[i] != heightsSorted[i]) ans++;
//         }
//         return ans;
    }
};
