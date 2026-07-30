class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """

        pushes=0

        for i in range (len(word)):
            pushes=pushes+(i//8)+1

        return pushes
        