# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """按行转化为柱状图，每行调用单调栈求最大矩形。"""

    # 定义 maximalRectangle 函数/方法。
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not matrix or not matrix[0]:
            # 返回当前函数结果。
            return 0
        # 初始化或更新变量 n。
        n = len(matrix[0])
        # 初始化或更新变量 heights。
        heights = [0] * n
        # 初始化或更新变量 ans。
        ans = 0

        # 遍历当前序列，逐步推进状态。
        for row in matrix:
            # 遍历当前序列，逐步推进状态。
            for j, ch in enumerate(row):
                # 执行当前语句，更新算法状态。
                heights[j] = heights[j] + 1 if ch == '1' else 0
            # 初始化或更新变量 ans。
            ans = max(ans, self._largest_rectangle_area(heights))
        # 返回当前函数结果。
        return ans

    # 定义 _largest_rectangle_area 函数/方法。
    def _largest_rectangle_area(self, heights: List[int]) -> int:
        # 初始化或更新变量 stack: list[int]。
        stack: list[int] = []
        # 初始化或更新变量 ans。
        ans = 0
        # 初始化或更新变量 arr。
        arr = heights + [0]
        # 遍历当前序列，逐步推进状态。
        for i, h in enumerate(arr):
            # 当条件成立时循环处理，直到状态收敛。
            while stack and arr[stack[-1]] > h:
                # 弹出元素用于回退或继续计算。
                height = arr[stack.pop()]
                # 初始化或更新变量 left。
                left = stack[-1] if stack else -1
                # 初始化或更新变量 width。
                width = i - left - 1
                # 初始化或更新变量 ans。
                ans = max(ans, height * width)
            # 向容器末尾追加元素，扩展结果集合。
            stack.append(i)
        # 返回当前函数结果。
        return ans


# 定义 SolutionDPWidth 类，封装该题解法。
class SolutionDPWidth:
    """预处理每格向左连续 1 的宽度，再向上枚举高度（易理解）。"""

    # 定义 maximalRectangle 函数/方法。
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not matrix or not matrix[0]:
            # 返回当前函数结果。
            return 0
        # 初始化或更新变量 m, n。
        m, n = len(matrix), len(matrix[0])
        # 初始化或更新变量 left。
        left = [[0] * n for _ in range(m)]
        # 初始化或更新变量 ans。
        ans = 0

        # 遍历当前序列，逐步推进状态。
        for i in range(m):
            # 遍历当前序列，逐步推进状态。
            for j in range(n):
                # 判断条件是否成立，选择对应处理分支。
                if matrix[i][j] == '1':
                    # 初始化或更新变量 left[i][j]。
                    left[i][j] = (left[i][j - 1] + 1) if j > 0 else 1
                    # 初始化或更新变量 width。
                    width = left[i][j]
                    # 遍历当前序列，逐步推进状态。
                    for k in range(i, -1, -1):
                        # 判断条件是否成立，选择对应处理分支。
                        if left[k][j] == 0:
                            # 终止当前循环，进入后续流程。
                            break
                        # 初始化或更新变量 width。
                        width = min(width, left[k][j])
                        # 初始化或更新变量 ans。
                        ans = max(ans, width * (i - k + 1))
        # 返回当前函数结果。
        return ans


if __name__ == "__main__":
    solution = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(solution.maximalRectangle(matrix))
