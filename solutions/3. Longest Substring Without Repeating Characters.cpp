class Solution {
public:
    // "abba"
    int lengthOfLongestSubstring(string s) {
        int leftBound = -1, ans = 0; 
        unordered_map<char,int> lookup;
        for (int i=0; i<s.size(); i++) {
            char c=s[i];
            if (lookup.contains(c)) {
                leftBound = max(leftBound, lookup[c]);
            }
            ans = max(ans, i - leftBound);
            lookup[c] = i;
        }
        return ans;
    }
};
​
class Solution {
public:
    // //LeetCode sliding window optimized, time O(N), space O(M,N)
    // int lengthOfLongestSubstring(string s) {
    //     int n = s.length();
    //     unordered_map<int, int> map;
    //     int c = 0, maxlen = -1;
    //     for (int i = 0; i < n; i++) {
    //         if (map.find(s[i]) == map.end() || (i - map[s[i]] > c))
    //             c++;
    //         else {
    //             maxlen = max(maxlen, c);
    //             c = i-map[s[i]];
    //         }
    //         map[s[i]] = i;
    //     }   
    //     return max(maxlen, c);
    // }
    
//     //LeetCode sliding window, time O(N), space O(M,N)
//     int lengthOfLongestSubstring(string s) {
//         vector<int> chars(128);
//         int left = 0;
//         int right = 0;
//         int ans = 0;
        
//         while (right < s.length()) {
//             char r = s[right];
//             chars[r]++;
            
