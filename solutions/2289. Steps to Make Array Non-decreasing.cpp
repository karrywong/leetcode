class Solution {
public:
    int totalSteps(vector<int>& nums) {
        // [5,4,3,2,1] -> [5]
        // [5,1,2,3,4] -> [5,2,3,4] -> [5,3,4] ->... -> [5]
        
        // Vlad - monotonic stack and dp
        vector<array<int,2>> st;
        
        for (int i = nums.size()-1; i > -1; --i){
            int cnt = 0;
            while(!st.empty() && st.back()[1] < nums[i]) {
                cnt = max(cnt+1, st.back()[0]);
                st.pop_back();
            }
            st.push_back({cnt, nums[i]});
        }
        return (*max_element(st.begin(), st.end()))[0];
        
        // // Failed attempt, without considering indices
        // vector<int> monoStack;
        // int ans=0;
        // for (int i = nums.size()-1; i > -1; --i){
        //     if (monoStack.empty()) {
        //         monoStack.push_back(nums[i]);
        //         continue;
        //     }
        //     int cnt = 0;
        //     while (!monoStack.empty() && monoStack.back() < nums[i]) {
        //         monoStack.pop_back();
        //         cnt += 1;
        //     }
        //     ans = max(ans, cnt);
        //     monoStack.push_back(nums[i]);
        // }
        // return ans;
    }
};
