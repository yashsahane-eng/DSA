1class Solution {
2public:
3    int removeDuplicates(vector<int>& nums) {
4        int n=nums.size();
5        int i=0;
6
7        for(int j=1 ;j<n;j++){
8            if(nums[j] != nums[i]){
9                nums[i+1]=nums[j];
10                i++;
11            }
12        }
13        return i+1;
14        
15    }
16};