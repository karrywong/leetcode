class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0, j = numbers.size()-1;
        int total = numbers[i] + numbers[j];
        while (total != target) {
            if (total < target) {
                i++;
            }
            else {
                j--;
            }
            total = numbers[i] + numbers[j];
        }
        return {i+1, j+1};
    }
};
