class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        int maxArea=0 ,maxDig=0;

        int n=dimensions.size();

        for(int i=0 ;i<n;i++){
            int l=dimensions[i][0];
            int w=dimensions[i][1];
            int currDig=l*l+w*w;

            if(currDig>maxDig || (currDig==maxDig && l*w>maxArea)){
                maxDig=currDig;
                maxArea=l*w;
            }
        }
        return maxArea;
        
    }
};