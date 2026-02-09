1class Solution {
2public:
3    vector<int> twoSum(vector<int>& nums, int target) {
4        int n = nums.size();
5
6        vector<int> ans;
7        for (int i = 0; i < n; i++) {
8            for (int j = i + 1; j < n; j++) {
9                if (nums[i] + nums[j] == target) {
10                    ans.push_back(i);
11                    ans.push_back(j);
12                    return ans;
13                }
14            }
15        }
16        return {-1, -1};
17    }
18};