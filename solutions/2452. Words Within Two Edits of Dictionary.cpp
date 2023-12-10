class Solution {
public:
    // votrubac Trie
    struct Trie {
        Trie* ch[26] = {};
        void insert(const string& s, int i=0) {
            if (i < s.size()) {
                if (ch[s[i] - 'a'] == nullptr)
                     ch[s[i] - 'a'] = new Trie();
                ch[s[i]-'a']->insert(s, i+1);
            }
        }
        bool match(const string& s, int cnt, int i=0){
            if (cnt < 0 || i == s.size())
                return cnt >= 0;
            bool res = false;
            for (int j=0; j<26; j++) {
                if (ch[j] != nullptr) {
                    res |= ch[j]->match(s, cnt - (j != s[i] - 'a'), i+1);
                }
            }
            return res;
        }
    };
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        vector<string> res;
        Trie t;
        for (const auto& d:dictionary) {
            t.insert(d);
        }
        for(const auto& q:queries){
            if (t.match(q,2)) {
                res.push_back(q);
            }
        }
        return res;
    }
};
