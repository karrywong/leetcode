class Solution {
public:
    bool isPerfectSquare(int num) {
        // sqrt(2^31 - 1) = 46340.9
        int l = 1, r = min(num,46340);
        while (l <= r) {
            int mid = l + (r-l) / 2;
            int midSq = mid * mid;
            if (midSq == num)
                return true;
            else if (midSq < num)
                l = mid+1;
            else
                r = mid-1;
        }
        return false;
    }
};
