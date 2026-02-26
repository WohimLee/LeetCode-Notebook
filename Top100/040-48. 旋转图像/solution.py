from __future__ import annotations

from typing import List


class Solution:
    """先转置，再每行反转。"""

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()


class SolutionLayerByLayer:
    """按圈四点交换。"""

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for layer in range(n // 2):
            first, last = layer, n - 1 - layer
            for j in range(first, last):
                offset = j - first
                top = matrix[first][j]
                matrix[first][j] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[j][last]
                matrix[j][last] = top

