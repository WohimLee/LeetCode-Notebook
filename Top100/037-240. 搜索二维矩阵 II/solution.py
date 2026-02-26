from __future__ import annotations

from bisect import bisect_left
from typing import List


class Solution:
    """从右上角开始走：每步排除一行或一列。"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            x = matrix[i][j]
            if x == target:
                return True
            if x > target:
                j -= 1
            else:
                i += 1
        return False


class SolutionRowBinarySearch:
    """逐行二分（利用每行有序）。"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for row in matrix:
            if row[0] <= target <= row[-1]:
                idx = bisect_left(row, target)
                if idx < len(row) and row[idx] == target:
                    return True
        return False

