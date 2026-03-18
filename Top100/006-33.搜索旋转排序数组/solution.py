# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """解法一（推荐）：一次二分，判断哪一侧有序。"""

    # 定义 search 函数/方法。
    def search(self, nums: List[int], target: int) -> int:
        # 初始化或更新变量 left, right。
        left, right = 0, len(nums) - 1

        # 当条件成立时循环处理，直到状态收敛。
        while left <= right:
            # 初始化或更新变量 mid。
            mid = (left + right) // 2
            # 判断条件是否成立，选择对应处理分支。
            if nums[mid] == target:
                # 返回当前函数结果。
                return mid

            # 判断条件是否成立，选择对应处理分支。
            if nums[left] <= nums[mid]:
                # 判断条件是否成立，选择对应处理分支。
                if nums[left] <= target < nums[mid]:
                    # 初始化或更新变量 right。
                    right = mid - 1
                # 执行上述条件均不满足时的兜底逻辑。
                else:
                    # 初始化或更新变量 left。
                    left = mid + 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 判断条件是否成立，选择对应处理分支。
                if nums[mid] < target <= nums[right]:
                    # 初始化或更新变量 left。
                    left = mid + 1
                # 执行上述条件均不满足时的兜底逻辑。
                else:
                    # 初始化或更新变量 right。
                    right = mid - 1
        # 返回当前函数结果。
        return -1


# 定义 SolutionPivot 类，封装该题解法。
class SolutionPivot:
    """解法二：先找旋转点，再做一次普通二分。"""

    # 定义 search 函数/方法。
    def search(self, nums: List[int], target: int) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not nums:
            # 返回当前函数结果。
            return -1

        # 初始化或更新变量 n。
        n = len(nums)
        # 初始化或更新变量 pivot。
        pivot = self._find_pivot(nums)

        # 判断条件是否成立，选择对应处理分支。
        if nums[pivot] <= target <= nums[n - 1]:
            # 返回当前函数结果。
            return self._binary_search(nums, pivot, n - 1, target)
        # 返回当前函数结果。
        return self._binary_search(nums, 0, pivot - 1, target)

    # 定义 _find_pivot 函数/方法。
    def _find_pivot(self, nums: List[int]) -> int:
        # 初始化或更新变量 left, right。
        left, right = 0, len(nums) - 1
        # 当条件成立时循环处理，直到状态收敛。
        while left < right:
            # 初始化或更新变量 mid。
            mid = (left + right) // 2
            # 判断条件是否成立，选择对应处理分支。
            if nums[mid] > nums[right]:
                # 初始化或更新变量 left。
                left = mid + 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 right。
                right = mid
        # 返回当前函数结果。
        return left

    # 定义 _binary_search 函数/方法。
    def _binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        # 当条件成立时循环处理，直到状态收敛。
        while left <= right:
            # 初始化或更新变量 mid。
            mid = (left + right) // 2
            # 判断条件是否成立，选择对应处理分支。
            if nums[mid] == target:
                # 返回当前函数结果。
                return mid
            # 判断条件是否成立，选择对应处理分支。
            if nums[mid] < target:
                # 初始化或更新变量 left。
                left = mid + 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 right。
                right = mid - 1
        # 返回当前函数结果。
        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(solution.search(nums, target))
