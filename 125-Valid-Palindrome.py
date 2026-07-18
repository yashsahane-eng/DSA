class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned=[]

        for ch in s:
            if ch .isalnum():
                cleaned.append(ch.lower())
            
        
        cleaned=" ".join(cleaned)
        return cleaned==cleaned[::-1]

        