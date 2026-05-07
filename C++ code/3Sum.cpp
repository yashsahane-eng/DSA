1class Solution {
2public:
3    vector<vector<int>> threeSum(vector<int>& nums) {
4        vector<vector<int>> ans;
5
6        int n = nums.size();
7
8        sort(nums.begin(), nums.end());
9
10        for (int i = 0; i < n; i++) {
11
12            if (i > 0 && nums[i] == nums[i - 1])
13                continue;
14
15            int j = i + 1;
16            int k = n - 1;
17
18            while (j < k) {
19                int sum = nums[i] + nums[j] + nums[k];
20
21                if (sum < 0) {
22                    j++;
23                } else if (sum > 0) {
24                    k--;
25                } else {
26
27                    vector<int> temp = {nums[i], nums[j], nums[k]};
28                    ans.push_back(temp);
29
30                    j++;
31                    k--;
32                    while (j < k && nums[j] == nums[j - 1])
33                        j++;
34                    while (j < k && nums[k] == nums[k + 1])
35                        k--;
36                }
37            }
38        }
39        return ans;
40    }
41};