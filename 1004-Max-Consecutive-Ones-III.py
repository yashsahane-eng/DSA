class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        maxLen=0

        for i in range(n):
            zeros=0

            for j in range(i,n):

                if nums[j]==0:
                    zeros+=1

                if zeros <=k:
                    Len=j-i+1

                    maxLen=max(maxLen , Len)

                else:
                    break

        return maxLen
        