class Solution {
public:
    double findMedianOneArray(vector<int>& nums) {
        int p = nums.size();
        int pHalf = p/2;
        return p % 2 ? nums[pHalf] : 0.5*(nums[pHalf-1]+nums[pHalf]);  
    } 
    double findMedian(vector<int>& A, vector<int>& B) {
        int i=0, j=0, m=A.size(), n=B.size(), halfLen = (m+n)/2, ans;
        while (i<m || j<n) {
            if (i+j == halfLen) {
                if (i<m && j<n) {
                    ans = min(A[i], B[j]);
                }
                else {
                    ans = i==m ? B[j] : A[i];
                }
                break;
            }
            
            if (i<m && j < n) {
                if (A[i] <= B[j]) i+=1;
                else j+=1;
            }
            else {
                if (i==m) j+=1;
                else i+=1;
            }
        }
        return ans;
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size()==0) {
            return findMedianOneArray(nums2);
        }
        if (nums2.size()==0) {
            return findMedianOneArray(nums1);
        }
        
        double ans;
        int m=nums1.size(), n=nums2.size(), lenSum = m+n;
        if (lenSum % 2) {
            ans = findMedian(nums1, nums2);
        } else {
            double val1, val2;
            if (nums1.back() < nums2.back()) {
                vector<int> vec(nums2.size()-1);
                std::copy(nums2.begin(), nums2.end()-1, vec.begin());
                val1 = findMedian(nums1,vec);
            } else {
                vector<int> vec(nums1.size()-1);
                std::copy(nums1.begin(), nums1.end()-1, vec.begin());
                val1 = findMedian(vec, nums2);
            }
            
            if (nums1[0] < nums2[0]) {
                vector<int> vec(nums1.size()-1);
                std::copy(nums1.begin()+1, nums1.end(), vec.begin());
                val2 = findMedian(vec, nums2);
            } else {
                vector<int> vec(nums2.size()-1);
                std::copy(nums2.begin()+1, nums2.end(), vec.begin());
                val2 = findMedian(nums1, vec);                
            }
            ans = 0.5*(val1+val2);
        }
        return ans;
    }
};
