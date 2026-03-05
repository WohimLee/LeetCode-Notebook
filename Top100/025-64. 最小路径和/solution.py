# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """二维 DP。"""

    # 定义 minPathSum 函数/方法。
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 初始化或更新变量 m, n。
        m, n = len(grid), len(grid[0])
        # 初始化或更新变量 dp。
        dp = [[0] * n for _ in range(m)]
        # 初始化或更新变量 dp[0][0]。
        dp[0][0] = grid[0][0]

        # 遍历当前序列，逐步推进状态。
        for i in range(1, m):
            # 初始化或更新变量 dp[i][0]。
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        # 遍历当前序列，逐步推进状态。
        for j in range(1, n):
            # 初始化或更新变量 dp[0][j]。
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 遍历当前序列，逐步推进状态。
        for i in range(1, m):
            # 遍历当前序列，逐步推进状态。
            for j in range(1, n):
                # 初始化或更新变量 dp[i][j]。
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # 返回当前函数结果。
        return dp[-1][-1]


# 定义 SolutionRollingDP 类，封装该题解法。
class SolutionRollingDP:
    """一维滚动 DP。"""

    # 定义 minPathSum 函数/方法。
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 初始化或更新变量 m, n。
        m, n = len(grid), len(grid[0])
        # 初始化或更新变量 dp。
        dp = [0] * n
        # 初始化或更新变量 dp[0]。
        dp[0] = grid[0][0]
        # 遍历当前序列，逐步推进状态。
        for j in range(1, n):
            # 初始化或更新变量 dp[j]。
            dp[j] = dp[j - 1] + grid[0][j]

        # 遍历当前序列，逐步推进状态。
        for i in range(1, m):
            # 更新变量 dp[0]，推进当前状态。
            dp[0] += grid[i][0]
            # 遍历当前序列，逐步推进状态。
            for j in range(1, n):
                # 初始化或更新变量 dp[j]。
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        # 返回当前函数结果。
        return dp[-1]

