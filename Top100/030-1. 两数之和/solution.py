from __future__ import annotations

from typing import List


class Solution:
    """哈希表：记录已经见过的数字下标。"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos: dict[int, int] = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in pos:
                return [pos[need], i]
            pos[x] = i
        return []


class SolutionSortTwoPointers:
    """排序 + 双指针（保留下标）。"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = sorted((x, i) for i, x in enumerate(nums))
        l, r = 0, len(arr) - 1
        while l < r:
            s = arr[l][0] + arr[r][0]
            if s == target:
                return [arr[l][1], arr[r][1]]
            if s < target:
                l += 1
            else:
                r -= 1
        return []

