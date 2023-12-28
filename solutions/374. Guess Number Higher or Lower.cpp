/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return       -1 if num is higher than the picked number
 *                1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
​
class Solution {
public:
//     better
    int guessNumber(int n) {
        int l = 1, r = n;
        while (l < r) {
            int mid = l + (r-l)/2;
            int guessAns = guess(mid);
            if (guessAns == 0) 
                return mid;
            else if (guessAns == 1)
                l = mid + 1;
            else
                r = mid - 1;
        }
        return l;
    }
//     bad
//     int guessNumber(int n) {
//         // initialization
//         int left = 1, right = n, mid=left+(right-left)/2;
//         int guessAns = guess(mid);
//         while (guessAns != 0) {
//             if (guessAns == 1) left = mid+1;
//             else if (guessAns == -1) right = mid;
//             mid = left+(right-left)/2;
//             guessAns = guess(mid);
            
//         }
//         return mid;
//     }
};
