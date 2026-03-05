# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """先转置，再每行反转。"""

    # 定义 rotate 函数/方法。
    def rotate(self, matrix: List[List[int]]) -> None:
        # 初始化或更新变量 n。
        n = len(matrix)
        # 遍历当前序列，逐步推进状态。
        for i in range(n):
            # 遍历当前序列，逐步推进状态。
            for j in range(i + 1, n):
                # 初始化或更新变量 matrix[i][j], matrix[j][i]。
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 遍历当前序列，逐步推进状态。
        for row in matrix:
            # 调用函数/方法，推进当前步骤。
            row.reverse()


# 定义 SolutionLayerByLayer 类，封装该题解法。
class SolutionLayerByLayer:
    """按圈四点交换。"""

    # 定义 rotate 函数/方法。
    def rotate(self, matrix: List[List[int]]) -> None:
        # 初始化或更新变量 n。
        n = len(matrix)
        # 遍历当前序列，逐步推进状态。
        for layer in range(n // 2):
            # 初始化或更新变量 first, last。
            first, last = layer, n - 1 - layer
            # 遍历当前序列，逐步推进状态。
            for j in range(first, last):
                # 初始化或更新变量 offset。
                offset = j - first
                # 初始化或更新变量 top。
                top = matrix[first][j]
                # 初始化或更新变量 matrix[first][j]。
                matrix[first][j] = matrix[last - offset][first]
                # 初始化或更新变量 matrix[last - offset][first]。
                matrix[last - offset][first] = matrix[last][last - offset]
                # 初始化或更新变量 matrix[last][last - offset]。
                matrix[last][last - offset] = matrix[j][last]
                # 初始化或更新变量 matrix[j][last]。
                matrix[j][last] = top

