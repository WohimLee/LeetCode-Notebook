# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
import math


# 定义 Solution 类，封装该题解法。
class Solution:
    """组合数学：总共走 m+n-2 步，选 m-1 步向下（或 n-1 步向右）。"""

    # 定义 uniquePaths 函数/方法。
    def uniquePaths(self, m: int, n: int) -> int:
        # 返回当前函数结果。
        return math.comb(m + n - 2, m - 1)


# 定义 SolutionDP 类，封装该题解法。
class SolutionDP:
    """一维 DP。"""

    # 定义 uniquePaths 函数/方法。
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化或更新变量 dp。
        dp = [1] * n
        # 遍历当前序列，逐步推进状态。
        for _ in range(1, m):
            # 遍历当前序列，逐步推进状态。
            for j in range(1, n):
                # 更新变量 dp[j]，推进当前状态。
                dp[j] += dp[j - 1]
        # 返回当前函数结果。
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(3, 7))
