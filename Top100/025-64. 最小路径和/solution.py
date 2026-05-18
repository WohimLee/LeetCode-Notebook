from __future__ import annotations

from typing import List

class Solution:
    """二维 DP。"""

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                # 当前位置只能从上边或左边走过来。
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

class SolutionRollingDP:
    """一维滚动 DP。"""

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                # dp[j] 是“上方”的旧值，dp[j-1] 是“左侧”的新值。
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(solution.minPathSum(grid))
