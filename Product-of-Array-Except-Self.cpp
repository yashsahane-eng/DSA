1class Solution {
2public:
3    vector<int> productExceptSelf(vector<int>& nums) {
4        int n=nums.size();
5        vector<int>ans(n,1);
6        //vector<int>prefix;       
7        for(int i=1;i<n;i++){
8          ans[i]=ans[i-1]*nums[i-1] ;
9        }
10        int suffix=1;
11        for(int i=n-2 ;i>=0 ;i--){
12            suffix*=nums[i+1];
13            ans[i]*=suffix;
14        }
15         
16        
17        return ans;
18    }
19};