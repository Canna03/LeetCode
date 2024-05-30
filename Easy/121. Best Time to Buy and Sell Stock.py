from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for high in prices:
            if low > high:
                low = high
            if high - low > profit:
                profit = high - low
        return profit