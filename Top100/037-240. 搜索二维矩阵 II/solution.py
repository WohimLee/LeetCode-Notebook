# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from bisect import bisect_left
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """从右上角开始走：每步排除一行或一列。"""

    # 定义 searchMatrix 函数/方法。
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 判断条件是否成立，选择对应处理分支。
        if not matrix or not matrix[0]:
            # 返回当前函数结果。
            return False
        # 初始化或更新变量 m, n。
        m, n = len(matrix), len(matrix[0])
        # 初始化或更新变量 i, j。
        i, j = 0, n - 1
        # 当条件成立时循环处理，直到状态收敛。
        while i < m and j >= 0:
            # 初始化或更新变量 x。
            x = matrix[i][j]
            # 判断条件是否成立，选择对应处理分支。
            if x == target:
                # 返回当前函数结果。
                return True
            # 判断条件是否成立，选择对应处理分支。
            if x > target:
                # 更新变量 j，推进当前状态。
                j -= 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 更新变量 i，推进当前状态。
                i += 1
        # 返回当前函数结果。
        return False


# 定义 SolutionRowBinarySearch 类，封装该题解法。
class SolutionRowBinarySearch:
    """逐行二分（利用每行有序）。"""

    # 定义 searchMatrix 函数/方法。
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 判断条件是否成立，选择对应处理分支。
        if not matrix or not matrix[0]:
            # 返回当前函数结果。
            return False
        # 遍历当前序列，逐步推进状态。
        for row in matrix:
            # 判断条件是否成立，选择对应处理分支。
            if row[0] <= target <= row[-1]:
                # 初始化或更新变量 idx。
                idx = bisect_left(row, target)
                # 判断条件是否成立，选择对应处理分支。
                if idx < len(row) and row[idx] == target:
                    # 返回当前函数结果。
                    return True
        # 返回当前函数结果。
        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    print(solution.searchMatrix(matrix, 5))
