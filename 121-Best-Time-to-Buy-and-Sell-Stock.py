class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        

        maxProfit=0
        mini=prices[0]
        n=len(prices)

        for i in range (1, n):

            curProfit=prices[i]-mini

            maxProfit=max(maxProfit,curProfit)

            mini=min(mini ,prices[i])

        return maxProfit