class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n=len(fruits)

        maxLen=0

        mpp={}

        l,r=0,0

        while r<n:
            mpp[fruits[r]]=mpp.get(fruits[r],0)+1

            if len(mpp)>2:
                mpp[fruits[l]]-=1
                if mpp[fruits[l]]==0:
                    del mpp[fruits[l]]
                l+=1

            if len(mpp)<=2:
                Len=r-l+1
                maxLen=max(maxLen,Len)

            r+=1

        return maxLen
