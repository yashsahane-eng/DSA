class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)

        maxLen=0 

        for i in range (n):

            hash_set = [0] * 256


            for j in range(i,n):

                if hash_set[ord(s[j])]==1:
                    break

                hash_set[ord(s[j])]=1

                curr_Len=j-i+1

                maxLen=max(maxLen , curr_Len)

        return maxLen
        