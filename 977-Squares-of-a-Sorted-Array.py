class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left =0 
        right=len(nums)-1
        result=[0]*len(nums)
        index=len(nums)-1

        while left<=right:
            leftSquare=nums[left]*nums[left]
            rightSquare=nums[right]*nums[right]

            if leftSquare>rightSquare:
                result[index]=leftSquare
                left+=1

            else :
                result[index]=rightSquare
                right-=1

            index-=1

        return result
        