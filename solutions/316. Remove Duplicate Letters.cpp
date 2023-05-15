class Solution {
public:
    string removeDuplicateLetters(string s) {
        //step 1. for loop over, build dict
        unordered_map<char, int> m;
        for (int i = 0; i < s.size(); i++) m[s[i]] = i;        
        string ans = "";
        for (int i = 0; i < s.size(); i++) {
            char ch = s[i];
            if (ans.empty()) {
                ans += ch;
                continue;
            }
            else if (ans.find(ch) < ans.size()) {
                continue;
            } 
            // deletion criterion, charPrev = ans[-1], (A) if charPrev appears again using dict
            // (B) charPrev is larger than char. If (A) and (B) -> delete charPrev -> update charPrev
            while (!ans.empty() && ans.back() >= ch && i < m[ans.back()]) {
                ans.pop_back();
            }
            ans += ch;
        } 
        return ans;
    }
};
