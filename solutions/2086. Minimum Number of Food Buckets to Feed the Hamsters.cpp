class Solution {
public:
    int minimumBuckets(string hamsters) {
    // "H..H" -> "HX.H"
    // "HHH" -> -1 or "HH." -> -1 or ".HH"
        
    // hamster[i] -> hamster[i-1] == "X", pass 
    // if not, hamster[i+1] == ., ans += 1 and hamster[i+1] = "X"
    // if not, hamster[i-1] == hamster[i+1] == "H", return -1
        
    int l = hamsters.length();
    if (l == 1){
        if (hamsters == "H") return -1;
    }
        
    int ans = 0;
    for (int i=0; i < l; ++i) {
        char c = hamsters[i];
        
        if (c=='.' || c=='X') continue;
        // c == "H"
        if (i > 0 && hamsters[i-1] == 'X') continue;
        if (i < l-1) {
            if (hamsters[i+1] == '.') {
                ans += 1;
                hamsters[i+1] = 'X';
            } else if (i == 0) {
                return -1;
            } else if (hamsters[i-1] == '.') {
                ans += 1;
                // hamsters[i-1] = 'X';
            } else {
                return -1;
            }
        } else { // i == l-1
            if (hamsters[i-1] == '.') {
                ans += 1;
            } else {
                return -1;
            }
        }
    }
    return ans;
    }
