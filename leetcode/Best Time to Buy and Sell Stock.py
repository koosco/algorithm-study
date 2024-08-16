from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = prices[0]
        res = 0
        for i in range(1, len(prices)):
            x = max(0, prices[i] - min_v)
            res = x if not res else max(res, x)
            min_v = min(min_v, prices[i])
        return res
