from __future__ import annotations

from typing import List

class Solution:
    """单调栈一次扫描（末尾补 0 触发清栈）。"""

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[int] = []
        ans = 0
        arr = heights + [0]
        for i, h in enumerate(arr):
            while stack and arr[stack[-1]] > h:
                # 当前更矮柱子出现时，以栈顶为高的矩形右边界已经确定。
                height = arr[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                ans = max(ans, height * width)
            stack.append(i)
        return ans

class SolutionBoundaries:
    """预处理每个柱子的左右第一个更小元素。"""

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stack: list[int] = []

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                right[stack[-1]] = i
                stack.pop()
            # 出栈完成后，栈顶就是左侧第一个更小元素。
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        ans = 0
        for i, h in enumerate(heights):
            ans = max(ans, h * (right[i] - left[i] - 1))
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
