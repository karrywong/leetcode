class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // first attempt, time O(N), space O(N)
        if (nums.size() == 0) return 0;
        
        vector<pair<int, int>> record;
        int temp = nums[0], count = 1;
        for (int i = 1; i < nums.size(); i++){
            if (temp == nums[i]) count++;
            else {
                record.push_back(make_pair(temp,count));
                temp = nums[i];
                count = 1;
            }
        }
        record.push_back(make_pair(temp,count));
        int i = 0;
        for (auto tp:record) {
            if (tp.second > 2) tp.second = 2;
            for (int j = 0; j < tp.second; j++){
                nums[i++] = tp.first;
            }
        }
        return i;
    }
};
