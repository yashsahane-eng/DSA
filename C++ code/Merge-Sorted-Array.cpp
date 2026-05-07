1class Solution {
2public:
3    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
4         int i = m - 1;        
5        int j = n - 1;        
6        int k = m + n - 1;    
7
8       
9        while (i >= 0 && j >= 0) {
10            if (nums1[i] > nums2[j]) {
11
12                nums1[k] = nums1[i];
13                i--;
14            } else {
15                nums1[k] = nums2[j];
16                j--;
17            }
18            k--;
19        }
20
21        
22        while (j >= 0) {
23            nums1[k] = nums2[j];
24            j--;
25            k--;
26        }
27       
28    }
29};
30        
31        
32