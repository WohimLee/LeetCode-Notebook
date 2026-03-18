# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """单调栈一次扫描（末尾补 0 触发清栈）。"""

    # 定义 largestRectangleArea 函数/方法。
    def largestRectangleArea(self, heights: List[int]) -> int:
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


# 定义 SolutionBoundaries 类，封装该题解法。
class SolutionBoundaries:
    """预处理每个柱子的左右第一个更小元素。"""

    # 定义 largestRectangleArea 函数/方法。
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 初始化或更新变量 n。
        n = len(heights)
        # 初始化或更新变量 left。
        left = [-1] * n
        # 初始化或更新变量 right。
        right = [n] * n
        # 初始化或更新变量 stack: list[int]。
        stack: list[int] = []

        # 遍历当前序列，逐步推进状态。
        for i, h in enumerate(heights):
            # 当条件成立时循环处理，直到状态收敛。
            while stack and heights[stack[-1]] >= h:
                # 初始化或更新变量 right[stack[-1]]。
                right[stack[-1]] = i
                # 弹出元素用于回退或继续计算。
                stack.pop()
            # 初始化或更新变量 left[i]。
            left[i] = stack[-1] if stack else -1
            # 向容器末尾追加元素，扩展结果集合。
            stack.append(i)

        # 初始化或更新变量 ans。
        ans = 0
        # 遍历当前序列，逐步推进状态。
        for i, h in enumerate(heights):
            # 初始化或更新变量 ans。
            ans = max(ans, h * (right[i] - left[i] - 1))
        # 返回当前函数结果。
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
