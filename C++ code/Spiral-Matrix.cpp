1class Solution {
2public:
3    vector<int> spiralOrder(vector<vector<int>>& matrix) {
4     
5        int n=matrix.size();
6        int m=matrix[0].size();
7        int left=0 , right=m-1;
8        int top=0 , bottom=n-1;
9        vector<int> ans;
10
11        while( top<=bottom && left<=right){
12
13            for(int i=left ; i<=right ;i++){
14                ans.push_back(matrix[top][i]);
15            }
16            top++;
17
18            for(int i=top ;i<=bottom ;i++){
19                ans.push_back(matrix[i][right]);
20            }
21            right--;
22            if( top<=bottom){
23            for(int i=right ;i>=left ;i--){
24                ans.push_back(matrix[bottom][i]);
25            }
26            bottom--;
27            }
28            if(left<=right){
29            
30            for(int i=bottom;i>=top;i--){
31                ans.push_back(matrix[i][left]);
32            }
33            left++;
34            }
35        }
36        return ans;
37        
38    }
39};