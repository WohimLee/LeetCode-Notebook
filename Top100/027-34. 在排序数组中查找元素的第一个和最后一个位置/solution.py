from __future__ import annotations

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    """两次二分：找左边界和右边界。"""

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self._lower_bound(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = self._lower_bound(nums, target + 1) - 1
        return [left, right]

    def _lower_bound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


class SolutionBisect:
    """Python bisect 写法。"""

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_right(nums, target) - 1
        if l <= r and l < len(nums) and nums[l] == target:
            return [l, r]
        return [-1, -1]

