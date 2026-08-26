class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n=len(s)

        hash= [-1] * 256

        l=0
        r=0
        maxLen=0

        while r < n :

            if hash[ord(s[r])] !=-1:
                l=max(hash[ord(s[r])]+1 ,l)


            current_Len=r-l+1

            maxLen=max(maxLen , current_Len)

            hash[ord(s[r])]=r

            r+=1

        return maxLen
        