class Solution {
public:
    int maxJump(vector<int>& stones) {
        // [0,x] -> x
        // [0,x,y] -> y
        
        // [0,2,5,7] -> 5
        
        // [0,2,4,5,6,7] -> 4
        
        
        //     [0,2,5,6,7] -> [0,5,6,7,2] or [0,6,7,5,2]
        // diff: 2,3,1,1
        // max(-> max(2+3,1,1) <- max(2,3+1+1)) = 5
        
        // C(n-2,0) + C(n-2,1) +.. + C(n-2,n-2)= 2^(n-2) 
        
        // even [0,1,2,3], path [0,2,3,1,0]
        // odd [0,1,2,3,4], path [0,2,4,3,1,0]
        
        // cost = maximum of all diff {arr[2]-arr[0], arr[4]-arr[2], ..., arr[3]-arr[1], .... }
        
        int cost = stones[1]-stones[0];
        for (int i = 1; i+1 < stones.size(); i++) {
            cost = max(cost, stones[i+1]-stones[i-1]);
        }
        return cost;
    }
};
