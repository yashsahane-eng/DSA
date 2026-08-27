class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        maxLen=0
        r=0
        l=0
        zeros=0

        n=len(nums)

        while r<n:

            if nums[r]==0:
                zeros+=1

            while zeros >k:

                if nums[l]==0:
                    zeros+=1

                l+=1

                Len=r-l+1

                maxLen=max(Len , maxLen)

                r+=1

        return maxLen