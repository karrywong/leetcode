class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        // 2nd attempt, sliding window
        int ans=0, l=0, cnt=0;
        
        for (int i=0; i<nums.size(); i++) {
            if (nums[i] == 0) cnt+=1;
        
        while (cnt==2) {
            if (nums[l]==0) {
                cnt-=1;
            }
            l+=1;
        }
        ans = max(ans, i-l+1);
        }
        return ans;
        
        // First attempt, two-pointer, time O(N), space O(1)
        // int ans=0, cnt=0, zeroLastSeen=-1, zeroPos=-1;
        // for (int i=0; i<nums.size(); i++) {
        //     if (nums[i]==0) {
        //         if (cnt>0) {
        //             zeroLastSeen = zeroPos;
        //             zeroPos = i;
        //         }
        //         else {
        //             cnt += 1;
        //             zeroPos=i;
        //         }
        //     }
        //     ans = max(ans, i-zeroLastSeen);
        // }
        // return ans;
    }
};
