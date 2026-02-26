from __future__ import annotations

import math


class Solution:
    """组合数学：总共走 m+n-2 步，选 m-1 步向下（或 n-1 步向右）。"""

    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)


class SolutionDP:
    """一维 DP。"""

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]

