class Solution {
public:
    // check if there is a leading zero
    bool checkLeadingZero(const string& s) {
        // string needs to be "0x..."
        return (s.length() > 1 && s[0] == '0') ? true : false; 
    }
    
    // given first two numbers, check if the rest of string is additive in a deterministic way
    bool checkAdditive(int i, int j, const string& num) {
        string firstNumStr = num.substr(0,i);
        if (checkLeadingZero(firstNumStr)) return false;
        string secondNumStr = num.substr(i,j);
        if (checkLeadingZero(secondNumStr)) return false;
        long long sumCheck = stoll(firstNumStr) + stoll(secondNumStr);
        int k = to_string(sumCheck).length();
        string sumStr = num.substr(i+j, k);
        if (checkLeadingZero(sumStr) || stoll(sumStr) != sumCheck) return false;
        int ind = i + j + k; //index after the first three numbers
    
        while (ind < num.size()-1) {
            firstNumStr = secondNumStr;
            secondNumStr = sumStr;
            sumCheck = stoll(firstNumStr) + stoll(secondNumStr);
            k = to_string(sumCheck).length();
            // Make sure num.substr(ind, k) is valid
            if (ind+k > num.size()) return false;
            sumStr = num.substr(ind, k);
            if (checkLeadingZero(sumStr) || stoll(sumStr) != sumCheck) return false;
            ind += k;
        }
        return true;
    }
    
    bool isAdditiveNumber(string num) {
        int n = num.size();
        if (n < 3) return false;
        for (int i=1; i<=n-2; ++i) {
            for (int j=1; j<=n-2; ++j) {
                if (max(i,j) > n-i-j) break;
                bool check = checkAdditive(i, j, num);
                if (check) return true;
            }
        }
        return false;
    }
};
