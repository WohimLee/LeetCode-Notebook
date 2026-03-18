# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """标准 next_permutation。"""

    # 定义 nextPermutation 函数/方法。
    def nextPermutation(self, nums: List[int]) -> None:
        # 初始化或更新变量 i。
        i = len(nums) - 2
        # 当条件成立时循环处理，直到状态收敛。
        while i >= 0 and nums[i] >= nums[i + 1]:
            # 更新变量 i，推进当前状态。
            i -= 1

        # 判断条件是否成立，选择对应处理分支。
        if i >= 0:
            # 初始化或更新变量 j。
            j = len(nums) - 1
            # 当条件成立时循环处理，直到状态收敛。
            while nums[j] <= nums[i]:
                # 更新变量 j，推进当前状态。
                j -= 1
            # 初始化或更新变量 nums[i], nums[j]。
            nums[i], nums[j] = nums[j], nums[i]

        # 初始化或更新变量 l, r。
        l, r = i + 1, len(nums) - 1
        # 当条件成立时循环处理，直到状态收敛。
        while l < r:
            # 初始化或更新变量 nums[l], nums[r]。
            nums[l], nums[r] = nums[r], nums[l]
            # 更新变量 l，推进当前状态。
            l += 1
            # 更新变量 r，推进当前状态。
            r -= 1


# 定义 SolutionSortSuffix 类，封装该题解法。
class SolutionSortSuffix:
    """同一思路的直观版本：交换后对后缀排序。"""

    # 定义 nextPermutation 函数/方法。
    def nextPermutation(self, nums: List[int]) -> None:
        # 初始化或更新变量 i。
        i = len(nums) - 2
        # 当条件成立时循环处理，直到状态收敛。
        while i >= 0 and nums[i] >= nums[i + 1]:
            # 更新变量 i，推进当前状态。
            i -= 1

        # 判断条件是否成立，选择对应处理分支。
        if i >= 0:
            # 初始化或更新变量 j。
            j = len(nums) - 1
            # 当条件成立时循环处理，直到状态收敛。
            while nums[j] <= nums[i]:
                # 更新变量 j，推进当前状态。
                j -= 1
            # 初始化或更新变量 nums[i], nums[j]。
            nums[i], nums[j] = nums[j], nums[i]

        # 初始化或更新变量 nums[i + 1 :]。
        nums[i + 1 :] = sorted(nums[i + 1 :])


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    print(nums)
