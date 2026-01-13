class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = float('inf')
        res = 0

        for i in prices:
            if i < min:
                min = i
            else :
                res = max(res, i - min) 
        return res
