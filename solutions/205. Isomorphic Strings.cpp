class Solution {
public:
    bool isIsomorphic(string s, string t) {
//  s = "abc", t = "xxy", ans=false, not allow, "a"->"x" & "b"->"x"
    // 2nd attempt, idea arrS = [0,"a",..,], arrT = [,...,]
        char arrStoT[256] = {0};
        bool seenT[256] = {false};
        for (int i=0; i<t.length(); i++){
            const char sChar=s[i], tChar = t[i];
            bool checkS = (arrStoT[sChar] > 0 && arrStoT[sChar] != tChar) || (arrStoT[sChar] == 0 && seenT[tChar]);
                
            if (checkS) return false;
            arrStoT[sChar] = tChar;
            seenT[tChar] = true;
        }
        return true;
    }
        
//     // 1st attempt, time O(N), space O(N)
//         unordered_map<char, char> sTot;
//         unordered_set<char> seenT;
//         for (int i=0; i<t.length(); i++) {
//             const char sChar=s[i], tChar = t[i];
//             bool checkS = (sTot.contains(sChar) && sTot[sChar] != tChar) || (!sTot.contains(sChar) && seenT.contains(tChar));
            
//             if (checkS) return false;
//             sTot[sChar] = tChar;
//             seenT.insert(tChar);
//         }
//         return true;
// }
};
