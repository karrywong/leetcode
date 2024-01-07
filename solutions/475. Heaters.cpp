class Solution {
public:
    int getHeaters(int house, vector<int>& heaters) {
        // house=10, (0,3) -> (2,3) -> (3,3) -> 2
        // house=12, (0,3) -> 3 
        // house=1, heater=[3,4,11], (0,2)->(0,1)->(0,0) -> -1
        int l=0, r=heaters.size()-1;
        while (l < r) { // l=r
            int mid = l + (r-l)/2;
            if (heaters[mid] == house){
                l = mid;
                break;
            } else if (heaters[mid] > house)
                r = mid;
            else 
                l = mid+1;
        }
        return heaters[l] > house ? l-1 : l;
    }
​
    // time O(N * logM + M * logM) =, space O(1), N = house.size(), M = heaters.size()
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        // house = 10, heater = [1,3,4,11]
        // loop over houses 
        // for each house, find maximal number of heater lsq house        
        sort(heaters.begin(), heaters.end());
        int ans = 0;
        heaters.insert(heaters.begin(),-1*pow(10,9));
        heaters.push_back(INT_MAX);
        for (const auto h : houses) {
            int i = getHeaters(h, heaters), dist;
            dist = min(h-heaters[i], heaters[i+1]-h);
            ans = max(ans, dist);
        }
        return ans;
    }
};
