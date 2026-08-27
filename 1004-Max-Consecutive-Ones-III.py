class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)

        l,r=0,0
        zeros , maxLen=0,0

        while r<n :

            if nums[r]==0:
                zeros+=1

            if zeros > k:
                if nums[l]==0:
                    zeros-=1

                l+=1

            if zeros <=k:

                Len=r-l+1

                maxLen=max(Len , maxLen)

            r+=1

        return maxLen