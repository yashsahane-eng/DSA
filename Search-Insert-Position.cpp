class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left=0;
        int n=nums.size()-1;
        int right=n;

        while(left<=right){
            int mid=left+(right-left)/2;

            if (nums[mid]==target){
                return mid;

            }else if (nums[mid]>target){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        return left;
        
    }
};