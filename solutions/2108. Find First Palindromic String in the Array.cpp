class Solution {
public:
    bool isPalindrome(const string& word) {
        bool ans = true;
        int l = 0, r = word.size()-1;
        while (l < r) {
            if (word[l] != word[r]) {
                ans = false;
                break;
            }
            l++;
            r--;
        }
        return ans;
    }
    string firstPalindrome(vector<string>& words) {
        string ans = "";
        for (const auto word: words) {
            if (isPalindrome(word)) {
                ans = word;
                break;
            }
        }
        return ans;
    }
};
