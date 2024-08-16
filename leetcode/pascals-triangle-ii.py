from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] for _ in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
            dp[i].append(1)
        return dp

