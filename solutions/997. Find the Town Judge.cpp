class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        if (n==1) return 1;
        if (trust.size() < n-1) return -1;
        map<int, int> m;
        for (auto& t : trust) {
            m[t[0]] -= 1;
            m[t[1]] += 1;
        }
        for (auto i = m.begin(); i != m.end(); i++) {
            if (i->second == n-1) return i->first;
        }
        return -1;
    }
};
