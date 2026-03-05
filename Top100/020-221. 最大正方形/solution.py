# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """二维 DP：dp[i][j] 表示以该点为右下角的最大正方形边长。"""

    # 定义 maximalSquare 函数/方法。
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not matrix or not matrix[0]:
            # 返回当前函数结果。
            return 0
        # 初始化或更新变量 m, n。
        m, n = len(matrix), len(matrix[0])
        # 初始化或更新变量 dp。
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 初始化或更新变量 best。
        best = 0

        # 遍历当前序列，逐步推进状态。
        for i in range(1, m + 1):
            # 遍历当前序列，逐步推进状态。
            for j in range(1, n + 1):
                # 判断条件是否成立，选择对应处理分支。
                if matrix[i - 1][j - 1] == '1':
                    # 初始化或更新变量 dp[i][j]。
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    # 初始化或更新变量 best。
                    best = max(best, dp[i][j])
        # 返回当前函数结果。
        return best * best


# 定义 SolutionRollingDP 类，封装该题解法。
class SolutionRollingDP:
    """一维滚动 DP，空间优化到 O(n)。"""

    # 定义 maximalSquare 函数/方法。
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not matrix or not matrix[0]:
            # 返回当前函数结果。
            return 0
        # 初始化或更新变量 m, n。
        m, n = len(matrix), len(matrix[0])
        # 初始化或更新变量 dp。
        dp = [0] * (n + 1)
        # 初始化或更新变量 best。
        best = 0

        # 遍历当前序列，逐步推进状态。
        for i in range(1, m + 1):
            # 初始化或更新变量 prev_diag。
            prev_diag = 0
            # 遍历当前序列，逐步推进状态。
            for j in range(1, n + 1):
                # 初始化或更新变量 temp。
                temp = dp[j]
                # 判断条件是否成立，选择对应处理分支。
                if matrix[i - 1][j - 1] == '1':
                    # 初始化或更新变量 dp[j]。
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev_diag)
                    # 初始化或更新变量 best。
                    best = max(best, dp[j])
                # 执行上述条件均不满足时的兜底逻辑。
                else:
                    # 初始化或更新变量 dp[j]。
                    dp[j] = 0
                # 初始化或更新变量 prev_diag。
                prev_diag = temp
        # 返回当前函数结果。
        return best * best

