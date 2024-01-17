//             }
//             else {
//                 if (i==m) j+=1;
//                 else i+=1;
//             }
//         }
//         return ans;
//     }
//     double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
//         if (nums1.size()==0) {
//             return findMedianOneArray(nums2);
//         }
//         if (nums2.size()==0) {
//             return findMedianOneArray(nums1);
//         }
        
//         double ans;
//         int m=nums1.size(), n=nums2.size(), lenSum = m+n;
//         if (lenSum % 2) {
//             ans = findMedian(nums1, nums2);
//         } else {
//             double val1, val2;
//             if (nums1.back() < nums2.back()) {
//                 vector<int> vec(nums2.size()-1);
//                 std::copy(nums2.begin(), nums2.end()-1, vec.begin());
//                 val1 = findMedian(nums1,vec);
//             } else {
//                 vector<int> vec(nums1.size()-1);
//                 std::copy(nums1.begin(), nums1.end()-1, vec.begin());
//                 val1 = findMedian(vec, nums2);
//             }
            
//             if (nums1[0] < nums2[0]) {
//                 vector<int> vec(nums1.size()-1);
//                 std::copy(nums1.begin()+1, nums1.end(), vec.begin());
//                 val2 = findMedian(vec, nums2);
//             } else {
//                 vector<int> vec(nums2.size()-1);
//                 std::copy(nums2.begin()+1, nums2.end(), vec.begin());
//                 val2 = findMedian(nums1, vec);                
//             }
//             ans = 0.5*(val1+val2);
//         }
//         return ans;
//     }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        //solution with detailed explanation at NeetCode <https://youtu.be/q6IEA26hvXc>
        //Time complexity, O(log(M+N)) from binary search, see An-Wen Deng
        if (nums1.size() > nums2.size()) 
            return findMedianSortedArrays(nums2, nums1);
        
        int nA = nums1.size(), nB = nums2.size();
        int l = 0, r = nA;
        
        while (true) {
            int cutA = (l + r) / 2;
            int cutB = (nA + nB + 1) / 2 - cutA;
            
            int maxLeftA = (cutA == 0) ? INT_MIN : nums1[cutA - 1];
            int minRightA = (cutA == nA) ? INT_MAX : nums1[cutA];
            int maxLeftB = (cutB == 0) ? INT_MIN : nums2[cutB - 1];
            int minRightB = (cutB == nB) ? INT_MAX : nums2[cutB];
            
            if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
                if ((nA + nB) % 2 == 0) return 
                (max(maxLeftA, maxLeftB)+min(minRightA,minRightB))/2.0;
                else return max(maxLeftA, maxLeftB); 
            } 
            else if (maxLeftA > minRightB) 
                r = cutA - 1;
            else 
                l = cutA + 1;
        }
    }
};
