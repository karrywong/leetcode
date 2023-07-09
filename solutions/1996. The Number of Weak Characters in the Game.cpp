class Solution {
public:
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        int cnt = 0, n = properties.size(); // n >= 2
        std::sort(properties.begin(), properties.end(), [] (const auto& a, const auto& b) {
        return a[0] == b[0] ? a[1] < b[1] : a[0] > b[0];});      
                
        int fiNum = properties[0][0], maxSecSeen = properties[0][1];
        for (int i=1; i < n; i++){
            if (properties[i][0] == fiNum){
                maxSecSeen = properties[i][1];
                continue;
            }
            
            if (maxSecSeen > properties[i][1]) {
                cnt += 1;
            }
            else if (maxSecSeen < properties[i][1]) {
                maxSecSeen = properties[i][1];
                fiNum = properties[i][0];
            }
        }
        return cnt;
    }
};
​
​
// [[1,5],[4,3],[10,4],[10,5]]
// [[1,5],[4,3],[10,3],[10,4],[10,5], [11,7]]
// [[1,5],[4,3],[10,5],[10,8],[11,7]]
// [[1,5],[4,3],[9,15], [10,5],[10,8],[11,7],[11,9]]
// st = [5,3,5]
​
// [[10,1],[9,2],[8,3],[7,4],[11,11]]
​
// [[7,4],[8,3],[9,2],[10,1],[11,11]]
// st =[11]
  
// (6,9)
// (7,5)
// (7,9)
// (7,10)
// (10,4)
// (10,7)
​
