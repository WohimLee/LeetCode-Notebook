from __future__ import annotations

from typing import List


class Solution:
    """二维 DP：dp[i][j] 表示以该点为右下角的最大正方形边长。"""

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        best = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    best = max(best, dp[i][j])
        return best * best


class SolutionRollingDP:
    """一维滚动 DP，空间优化到 O(n)。"""

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        best = 0

        for i in range(1, m + 1):
            prev_diag = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev_diag)
                    best = max(best, dp[j])
                else:
                    dp[j] = 0
                prev_diag = temp
        return best * best

