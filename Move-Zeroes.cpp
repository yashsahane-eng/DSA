1class Solution {
2public:
3    void moveZeroes(vector<int>& nums) {
4        int slow = 0;
5        int n = nums.size();
6        for (int fast = 0; fast < n; fast++) {
7            if (nums[fast] != 0) {
8                nums[slow] = nums[fast];
9                slow++;
10            }
11        }
12        while (slow < n) {
13            nums[slow] = 0;
14            slow++;
15        }
16    }
17};