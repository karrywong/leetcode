            pair<int,int> h1(building[0], building[2]), h2(building[1], -1*building[2]);
            heights.push_back(h1);
            heights.push_back(h2);
        }
        
        sort(arr.begin(), arr.end());
        arr.erase(unique(arr.begin(), arr.end()), arr.end());
        sort(heights.begin(), heights.end());
        
        vector<vector<int>> street;
        int heightPos = 0, heightSum = 0, cnt = 0;
​
        for (int i=0; i<arr.size()-1; ++i) {
            for (;heightPos < heights.size(); ++heightPos){
                if (heights[heightPos].first == arr[i]) {
                    heightSum += heights[heightPos].second;
                    if (heights[heightPos].second > 0) {
                        cnt++; 
                    }
                    else {
                        cnt--;
                    }
                }
                else break;
            }
            if (cnt > 0) { // in the case of disjoint building like buildings = [[1,2,1],[5,6,1]]
                int heightAvg=heightSum/cnt;
                street.push_back({arr[i], arr[i+1], heightAvg});
            }
        }
        
        int i=1;
        vector<vector<int>> ans={street[0]};
        while (i < street.size()) {
            if (ans.back()[2] == street[i][2] && ans.back()[1] == street[i][0]) {
                ans.back()[1] = street[i][1];
            }
            else {
                ans.push_back(street[i]);
            }
            i++;
        }
        return ans;
        
    }
};
