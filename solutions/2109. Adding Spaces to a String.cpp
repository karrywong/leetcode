class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        // Vlad
        int last = 0;
        string res;
        for (const auto space : spaces) {
            res += s.substr(last, space - last) + " ";
            last = space;
        }
        res += s.substr(last);
        return res;
        
//         // my solution, time O(len(s) + len(spaces)), space O(len(s) + len(spaces))
//         vector<int> indices = {0};
//         for (const auto space : spaces) {
//             indices.push_back(space);
//         }
//         indices.push_back(s.size()); //{0,0,2,3,4,5}
        
//         vector<string> vec;
//         for (int i=0; i<indices.size()-1; i++) {
//             int h = indices[i], k = indices[i+1];
//             vec.push_back(s.substr(h, k-h));
//         }// {"", "YP", "A", "d", "f"}
//         string ans;
//         for (int i=0; i<vec.size()-1; i++) {
//             ans += vec[i] + " ";
//         }
//         ans += vec[vec.size()-1];
//         return ans;
    }   
};
