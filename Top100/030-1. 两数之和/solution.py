# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """哈希表：记录已经见过的数字下标。"""

    # 定义 twoSum 函数/方法。
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 初始化或更新变量 pos: dict[int, int]。
        pos: dict[int, int] = {}
        # 遍历当前序列，逐步推进状态。
        for i, x in enumerate(nums):
            # 初始化或更新变量 need。
            need = target - x
            # 判断条件是否成立，选择对应处理分支。
            if need in pos:
                # 返回当前函数结果。
                return [pos[need], i]
            # 初始化或更新变量 pos[x]。
            pos[x] = i
        # 返回当前函数结果。
        return []


# 定义 SolutionSortTwoPointers 类，封装该题解法。
class SolutionSortTwoPointers:
    """排序 + 双指针（保留下标）。"""

    # 定义 twoSum 函数/方法。
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 初始化或更新变量 arr。
        arr = sorted((x, i) for i, x in enumerate(nums))
        # 初始化或更新变量 l, r。
        l, r = 0, len(arr) - 1
        # 当条件成立时循环处理，直到状态收敛。
        while l < r:
            # 初始化或更新变量 s。
            s = arr[l][0] + arr[r][0]
            # 判断条件是否成立，选择对应处理分支。
            if s == target:
                # 返回当前函数结果。
                return [arr[l][1], arr[r][1]]
            # 判断条件是否成立，选择对应处理分支。
            if s < target:
                # 更新变量 l，推进当前状态。
                l += 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 更新变量 r，推进当前状态。
                r -= 1
        # 返回当前函数结果。
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
