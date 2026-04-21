1class Solution {
2public://Better Approach
3    void setZeroes(vector<vector<int>>& matrix) {
4        int m=matrix.size();
5        int n=matrix[0].size();
6
7        vector<int> row(m,0);
8        vector<int> col(n,0);
9
10        for(int i=0 ;i<m;i++){
11            for(int j=0 ;j<n;j++){
12
13                if(matrix[i][j]==0){
14                    row[i]=1;
15                    col[j]=1;
16                }
17            }
18        }
19        for(int i=0 ;i<m;i++){
20            for(int j=0 ;j<n;j++){
21                if(row[i]==1 || col[j]==1){
22                    matrix[i][j]=0;
23                }
24            }
25        }
26
27        
28    }
29};