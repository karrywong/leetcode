class Solution {
public:
    string addStrings(string num1, string num2) {
        int p1=num1.length()-1, p2=num2.length()-1, carry=0;
        vector<int> vec = {};
        while (p1 >= 0 or p2 >= 0 or carry) {
            int l1 = p1>=0 ? num1[p1]-'0' : 0;
            int l2 = p2>=0 ? num2[p2]-'0' : 0;
            int sumVal = l1+l2+carry;
            int rmd = sumVal % 10;
            carry = sumVal / 10;
            vec.push_back(rmd);
            p1 -= 1;
            p2 -= 1;
        } 
        string s;
        for (int i=vec.size()-1; i>-1; --i) {
            s += to_string(vec[i]);
        }
        return s;
    }
};
