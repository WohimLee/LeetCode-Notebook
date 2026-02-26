from __future__ import annotations

from typing import List


class Solution:
    """按行转化为柱状图，每行调用单调栈求最大矩形。"""

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        ans = 0

        for row in matrix:
            for j, ch in enumerate(row):
                heights[j] = heights[j] + 1 if ch == '1' else 0
            ans = max(ans, self._largest_rectangle_area(heights))
        return ans

    def _largest_rectangle_area(self, heights: List[int]) -> int:
        stack: list[int] = []
        ans = 0
        arr = heights + [0]
        for i, h in enumerate(arr):
            while stack and arr[stack[-1]] > h:
                height = arr[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                ans = max(ans, height * width)
            stack.append(i)
        return ans


class SolutionDPWidth:
    """预处理每格向左连续 1 的宽度，再向上枚举高度（易理解）。"""

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[i][j] = (left[i][j - 1] + 1) if j > 0 else 1
                    width = left[i][j]
                    for k in range(i, -1, -1):
                        if left[k][j] == 0:
                            break
                        width = min(width, left[k][j])
                        ans = max(ans, width * (i - k + 1))
        return ans

