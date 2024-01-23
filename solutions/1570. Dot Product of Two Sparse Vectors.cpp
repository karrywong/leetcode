class SparseVector {
public:
    vector<pair<int,int>> record; //{index, value}
    SparseVector(vector<int> &nums) {
        for (int i=0; i<nums.size(); ++i) {
            if (nums[i]) {
                record.push_back(std::make_pair(i, nums[i]));
            }
        }
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector& vec) {
        int res=0, i=0, j=0;
        while (i < record.size() && j < vec.record.size()) {
            if (record[i].first == vec.record[j].first) {
                res += record[i].second * vec.record[j].second;
                i++;
                j++;
            } else if (record[i].first < vec.record[j].first) {
                i++;
            } else {
                j++;
            }
        }
        return res;
    }
};
​
// Your SparseVector object will be instantiated and called as such:
// SparseVector v1(nums1);
// SparseVector v2(nums2);
// int ans = v1.dotProduct(v2);
