from __future__ import annotations

from typing import List


class Solution:
    """解法一（推荐）：一次二分，判断哪一侧有序。"""

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


class SolutionPivot:
    """解法二：先找旋转点，再做一次普通二分。"""

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)
        pivot = self._find_pivot(nums)

        if nums[pivot] <= target <= nums[n - 1]:
            return self._binary_search(nums, pivot, n - 1, target)
        return self._binary_search(nums, 0, pivot - 1, target)

    def _find_pivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left

    def _binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
