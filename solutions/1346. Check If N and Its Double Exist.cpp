class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        // Soln 2 - cleaner
        unordered_set<int> lookup;
        for (auto& a : arr) {
            if (lookup.count(a*2) || (a%2==0) && lookup.count(a/2)) 
                return true;
            lookup.insert(a);
        }
        return false;
        
        // // Soln 1 - 1st attempt, time O(N), space O(N)
        // unordered_set<int> seen;
        // for (int i = 0; i < arr.size(); ++i) {
        //     if (seen.find(arr[i]) != seen.end()) 
        //         return true;
        //     if (arr[i] % 2 == 0)
        //         seen.insert(arr[i]/2);
        //     seen.insert(arr[i] * 2);
        // }
        // return false;
    }
};
