class Solution {
public:
    long long taskSchedulerII(vector<int>& tasks, int space) {
        //  0,1,2,3,4,5 
        // [1,2,1,2,3,1]
        // {1:8, 2:9 }
        // days = 6
 
        //  0,1,2,3
        // [5,8,8,5]
        // {5:8, 8:7}
        // days = 6
        
        long long days = 0;
        unordered_map<int, long long> lookup; // key: task, val: "expiration date"
        for (const auto task: tasks) {
            if (lookup[task] > days) {
                days = lookup[task];
            }
            days += 1;
            lookup[task] = days + space;
        }
        return days;
    }
};
