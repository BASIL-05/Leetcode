class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=len(prices)
        
        max=0
        for i in range(l):
            if prices[i]>max:
                max=prices[i]
        low=max
        for i in range(prices.index(max)):
            if prices[i]<low:
                low=prices[i]
                
        return max-low
        
