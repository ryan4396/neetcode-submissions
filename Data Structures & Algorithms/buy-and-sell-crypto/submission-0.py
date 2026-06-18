class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        lowest_val = prices[0]
        for i in prices:
            if i - lowest_val > maxprofit:
                maxprofit = i-lowest_val
            if i < lowest_val:
                lowest_val = i
        return maxprofit