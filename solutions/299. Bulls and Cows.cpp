class Solution {
public:
    // key: digits, val: occurence
    //dS = {1: 1, 0: 1, 7: 1} 
    //dG = {7: 1, 1: 2, 0: 1}
    // Time O(secret.size()), space O(1)
    string getHint(string secret, string guess) {
        int n = secret.size(), x=0, y=0;
        unordered_map<char, int> mapSecret, mapGuess;
        for (int i = 0; i < n; ++i) {
            char s = secret[i], g = guess[i];
            if (s == g) x+=1;
            else {
                mapSecret[s]++;
                mapGuess[g]++;
            }
        }
        for (const auto pair : mapSecret) {
            char s = pair.first;
            if (mapGuess.find(s) != mapGuess.end()) {
                y += min(mapSecret[s], mapGuess[s]);
            }
        }
        string ans = to_string(x) + 'A' + to_string(y) + 'B';
        return ans;
    }
};
