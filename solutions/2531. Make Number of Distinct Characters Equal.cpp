class Solution {
public:
    bool isItPossible(string word1, string word2) {
        // Soln0 from votrubac
        int cnt1[26] = {}, cnt2[26] = {}, dist1 = 0, dist2 = 0;
        for (auto ch : word1)
            dist1 += ++cnt1[ch - 'a'] == 1;
        for (auto ch : word2)
            dist2 += ++cnt2[ch - 'a'] == 1;
            if (dist1 == dist2 && inner_product(begin(cnt1), end(cnt1), begin(cnt2), 0LL, plus<>(), multiplies<long long>())) 
            return true;
        for (int i = 0; i < 26; ++i)
            if (cnt1[i])
                for (int j = 0; j < 26; ++j)
                    if (cnt2[j])
                        if (i != j && dist1 - (cnt1[i] == 1) + (cnt1[j] == 0) ==
                           dist2 - (cnt2[j] == 1) + (cnt2[i] == 0))
                            return true;
        return false;
        
    }
};
​
// ac bb -> (2, 1) -> True
// ac bbb -> true
​
// abcc aab -> (3, 2)
// abccd aab -> (4, 2) -> abcca dab True
// abc aaa -> (3, 1) aba ac True
​
