class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        j = prices[0]
        x = 0 
        for i in range (1 ,len(prices)):
            x = max(x,prices[i]-j)

            if prices[i] < j :
                j = prices[i]
        return x
