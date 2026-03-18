# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from bisect import bisect_left, bisect_right
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """两次二分：找左边界和右边界。"""

    # 定义 searchRange 函数/方法。
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 初始化或更新变量 left。
        left = self._lower_bound(nums, target)
        # 判断条件是否成立，选择对应处理分支。
        if left == len(nums) or nums[left] != target:
            # 返回当前函数结果。
            return [-1, -1]
        # 初始化或更新变量 right。
        right = self._lower_bound(nums, target + 1) - 1
        # 返回当前函数结果。
        return [left, right]

    # 定义 _lower_bound 函数/方法。
    def _lower_bound(self, nums: List[int], target: int) -> int:
        # 初始化或更新变量 l, r。
        l, r = 0, len(nums)
        # 当条件成立时循环处理，直到状态收敛。
        while l < r:
            # 初始化或更新变量 mid。
            mid = (l + r) // 2
            # 判断条件是否成立，选择对应处理分支。
            if nums[mid] < target:
                # 初始化或更新变量 l。
                l = mid + 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 r。
                r = mid
        # 返回当前函数结果。
        return l


# 定义 SolutionBisect 类，封装该题解法。
class SolutionBisect:
    """Python bisect 写法。"""

    # 定义 searchRange 函数/方法。
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 初始化或更新变量 l。
        l = bisect_left(nums, target)
        # 初始化或更新变量 r。
        r = bisect_right(nums, target) - 1
        # 判断条件是否成立，选择对应处理分支。
        if l <= r and l < len(nums) and nums[l] == target:
            # 返回当前函数结果。
            return [l, r]
        # 返回当前函数结果。
        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
