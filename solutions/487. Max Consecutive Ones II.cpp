class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans=0, cnt=0, zeroLastSeen=-1, zeroPos=-1;
        for (int i=0; i<nums.size(); i++) {
            if (nums[i]==0) {
                if (cnt>0) {
                    zeroLastSeen = zeroPos;
                    zeroPos = i;
                }
                else {
                    cnt += 1;
                    zeroPos=i;
                }
            }
            ans = max(ans, i-zeroLastSeen);
        }
        return ans;
    }
};
