class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> heap;
        for (const auto num : nums){
            heap.push(-num);
            if (heap.size() > k) {
                heap.pop();
            }
        }
        return -heap.top();
    }
};
